import java.util.ArrayList;
import java.util.List;

/**
 * @author Sean Grimes on 9/19/17.
 * <p>Example main showing how to use the CashRegister.</p>
 */
public class Runner {
    public static void main(String[] args){
        // The below shows how to instantiate a new CashRegister and pay for an item

        // Instantiate a new CashRegister with the following bills / coins
        // Ones: 100
        // Fives: 10
        // Tens: 10
        // Twenties: 10
        // Fifties: 10
        // Hundreds: 10
        // Pennies: 1,000
        // Nickles: 100
        // Dimes: 100
        // Quarters: 10
        CashRegister cr = new CashRegister(100,10,10,10,10,10,1000,100,100,10);

        // Instantiate a BillPack, an object to hold the number and type of bills the user is using
        // to pay for their purchase. This one holds the following:
        // Ones: 0
        // Fives: 0
        // Tens: 0
        // Twenties: 0
        // Fifties: 0
        // Hundreds: 1
        BillPack purchaseBills = new BillPack(0, 0, 0, 0, 0, 1);

        // Instantial a CoinPack, an object to hold the number and type of coins the user is using
        // to pay for their purchase. This one holds the following:
        // Pennies: 0
        // Nickles: 0
        // Dimes: 0
        // Quarters: 0
        CoinPack purchaseCoins = new CoinPack(0, 0, 0, 0);

        // Try to purchase the notebook using the above BillPack and CoinPack, the CashRegister will
        // return the change to the user if the purchase is successful
        double notebookPrice = 10.57;
        double change = cr.purchaseItem(notebookPrice, purchaseBills, purchaseCoins);

        //------------------------------------------------------------------------------------------

        // The below shows how to instantiate a new CashRegister, scan multiple items, and complete
        // the purchase of multiple items. Note that a cash register can also be instantiated
        // with the BillPack and CoinPack objects instead of individual values for each type of
        // coin and bill
        BillPack crBills = new BillPack(10, 10, 10, 10, 10, 10);
        CoinPack crCoins = new CoinPack(1000, 100, 100, 100);

        CashRegister multiItems = new CashRegister(crBills, crCoins);

        // Create a list of item prices and item names. The cash register will keep track of the
        // item name and it's price as you scan new items before finalizing the purchase.
        List<Double> itemPrices = new ArrayList<>();
        List<String> itemNames = new ArrayList<>();

        itemPrices.add(10.00);
        itemNames.add("Expensive Soda");
        itemPrices.add(24.99);
        itemNames.add("Very Good Chocolate");
        itemPrices.add(0.89);
        itemNames.add("Very Bad Chocolate");

        // Run through the list of items, scan them into the cash register using their price and
        // name
        for(int i = 0; i < itemPrices.size(); ++i)
            multiItems.scanItem(itemPrices.get(i), itemNames.get(i));

        // The bills and coins the user will be using the purchase the above list of 3 items
        BillPack bills = new BillPack(1, 1, 2, 1, 0, 0);
        CoinPack coins = new CoinPack(10, 1, 2, 5);

        // Finalize the purchase and gather the returned change if the purchase is successful
        double multiChange = multiItems.finalizePurchase(bills, coins);
    }
}