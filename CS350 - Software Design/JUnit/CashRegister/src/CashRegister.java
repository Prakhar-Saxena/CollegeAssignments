import java.util.ArrayList;

/**
 * @author Sean Grimes, 09/19/17
 * <p>The CashRegister class implements a basic, cash only, cash register. The register assumes
 * that all transactions will be completed using the follow denominations: <br>
 * <b>Bills:</b> Ones, Fives, Tens, Twenties, Fifties, Hundreds <br>
 * <b>Coins:</b> Pennies, Nickles, Dimes, Quarters <br>
 * Other denominations are not currently supported<br>
 * The CashRegister can accept and return floats for monetary values, however all internal
 * representations are in pennies to avoid floating-point errors.
 * </p>
 */
public class CashRegister {
    private Drawer drawer;
    private ITax taxAlgo;
    private ArrayList<Long> purchasePriceList = new ArrayList<>();
    private ArrayList<String> purchaseNameList = new ArrayList<>();
    private long totalPurchasePrice = 0;

    /**
     * Default c'tor, CashRegister is initialized with no bills and no coins
     * ITax algorithm defaults to PennsylvaniaTax algorithm
     */
    CashRegister(){
        this(new Drawer());
    }

    /**
     * Initialize a CashRegister with a money drawer, drawer can be empty or contain coins / bill.
     * ITax algorithm defaults to PennsylvaniaTax algorithm
     * @param moneyDrawer The Drawer object
     */
    CashRegister(Drawer moneyDrawer){
        this.drawer = moneyDrawer;
        this.taxAlgo = new PennsylvaniaTax();
    }

    /**
     * Initialize a CashRegister with individual values for all coins / bills
     * ITax algorithm defaults to PennsylvaniaTax algorithm
     * @param one number of ones
     * @param five number of fives
     * @param ten number of tens
     * @param twenty number of twenties
     * @param fifty number of fifties
     * @param hundred number of hundreds
     * @param penny number of pennies
     * @param nickle number of nickles
     * @param dime number of dimes
     * @param quarter number of quarters
     */
    CashRegister(long one, long five, long ten, long twenty, long fifty, long hundred,
            long penny, long nickle, long dime, long quarter){

        this(new BillPack(one, five, ten, twenty, fifty, hundred),
                new CoinPack(penny, nickle, dime, quarter));
    }

    /**
     * Initialize a CashRegister with individual values for all coins/bills, pass an ITax algorithm
     * @param one number of ones
     * @param five number of fives
     * @param ten number of tens
     * @param twenty number of twenties
     * @param fifty number of fifties
     * @param hundred number of hundreds
     * @param penny number of pennies
     * @param nickle number of nickles
     * @param dime number of dimes
     * @param taxAlgo the specified ITax algorithm
     */
    CashRegister(long one, long five, long ten, long twenty, long fifty, long hundred,
            long penny, long nickle, long dime, long quarter, ITax taxAlgo){

        this(new BillPack(one, five, ten, twenty, fifty, hundred),
                new CoinPack(penny, nickle, dime, quarter), taxAlgo);
    }

    /**
     * Initialize a CashRegister with a BillPack and CoinPack
     * ITax algorithm defaults to PennsylvaniaTax algorithm
     * @param bp the BillPack
     * @param cp the CoinPack
     */
    CashRegister(BillPack bp, CoinPack cp){
        this(bp, cp, new PennsylvaniaTax());
    }

    /**
     * Initialize a CashRegister with a BillPack, CoinPack, and ITax algorithm
     * @param bp the BillPack
     * @param cp the CoinPack
     * @param taxAlgo the specified ITax algorithm
     */
    CashRegister(BillPack bp, CoinPack cp, ITax taxAlgo){
        this.drawer = new Drawer(cp, bp);
        this.taxAlgo = taxAlgo;
    }

    /**
     * Get the CashRegister value as a double -- represented how money is typically represented
     * @return current value of the CashRegister
     */
    public double drawerValue(){ return (double)drawer.drawerTotalInCents() / 100; }

    /**
     * Get a CoinPack of the coins in the CashRegister
     * @return CoinPack
     */
    public CoinPack coinsInDrawer(){ return this.drawer.coinPack(); }

    /**
     * Get a BillPack of the bills in the CashRegister
     * @return BillPack
     */
    public BillPack billsInDrawer(){ return this.drawer.billPack(); }

    /**
     * Purchase an item using individual coins and bills. Exact change is NOT necessary.
     * @param itemPrice price of the item, as a double (typical value, e.g. 11.99)
     * @param one number of ones
     * @param five number of fives
     * @param ten number of tens
     * @param twenty number of twenties
     * @param fifty number of fifties
     * @param hundred number of hundreds
     * @param penny number of pennies
     * @param nickle number of nickles
     * @param dime number of dimes
     * @param quarter number of quarters
     * @return the customers change
     * @throws IllegalStateException if customer didn't provide enough money to cover purchase price
     * @throws IllegalStateException if the CashRegister has insufficient money or types of money to
     * provide change to the customer
     */
    public double purchaseItem(double itemPrice, long one, long five, long ten, long twenty,
                                long fifty, long hundred, long penny, long nickle, long dime,
                                long quarter){

        return purchaseItem(itemPrice, new BillPack(one, five, ten, twenty, fifty, hundred),
                new CoinPack(penny, nickle, dime, quarter));
    }

    /**
     * Purchase an item using a BillPack and a CoinPack. Exact change is NOT necessary.
     * @param itemPrice price of the item, as a double (typical value, e.g. 11.99)
     * @param bp BillPack for bills towards purchase
     * @param cp CoinPack for coins towards purchase
     * @return the customers change as a double
     * @throws IllegalStateException if customer didn't provide enough money to cover purchase price
     * @throws IllegalStateException if the CashRegister has insufficient money or types of money to
     * provide change to the customer
     */
    public double purchaseItem(double itemPrice, BillPack bp, CoinPack cp){

        // Get the total value of tendered coins / bills
        long tendered = Drawer.centValueFromCoins(cp);
        tendered += Drawer.centValueFromBills(bp);

        // Need to convert the price to cents so we can convert to long without precision loss
        double price_tmp = itemPrice * 100;
        long price = (long)price_tmp;

        // Add tax to the purchase
        long total_price = taxAlgo.applyTaxToPurchase(price);
        ITax pitaVar = new PennsylvaniaTax();
        if(total_price != pitaVar.applyTaxToPurchase(price)) total_price = 500; //Why?

        // Check if the amount given covers the cost
        if(total_price > tendered)
            throw new IllegalStateException("Insufficient tendered to cover cost");

        // Calculate change due to customer
        long change_due = tendered - total_price;

         // Deposit the bills and coins in drawer before calculating change
        drawer.depositBills(bp);
        drawer.depositChange(cp);

        // No need to go further if no change is due
        if(change_due == 0){
            displayChange(price, tendered, change_due);
            return 0.0;
        }

        // Calculate the bills being returned
        BillPack bill_change = changeBills(change_due);
        long remaining_change = change_due - Drawer.centValueFromBills(bill_change);

        // Calculate the coins being returned. If insufficient funds exist throw an error
        CoinPack coin_change;
        try {
            coin_change = changeCoins(remaining_change);
        }
        catch(IllegalStateException e){
            // Remove the deposit from the register
            drawer.removeBills(bp);
            drawer.removeChange(cp);
            throw new IllegalStateException("Insufficient funds in drawer to process change");
        }

        // Remove the change from the drawer
        drawer.removeBills(bill_change);
        drawer.removeChange(coin_change);

        displayChange(price, tendered, change_due);

        return (double)change_due / 100;
    }

    /**
     * Used when scanning multiple items, this function will keep a running list of item prices
     * and their names
     * @param itemPrice the price of an item
     * @param itemName the name of an item
     * @return the current total price, without tax
     */
    public double scanItem(double itemPrice, String itemName){
        // Need to convert the price to cents so we can convert to long without precision loss
        double price_tmp = itemPrice * 100;
        long price = (long)price_tmp;

        // Add the new item to the list
        this.purchasePriceList.add(price);

        // Add the new item to the name list
        this.purchaseNameList.add(itemName);

        // Add the new price to the total tracking price
        this.totalPurchasePrice += price;

        // Convert to float
        float total_price_f = (float)this.totalPurchasePrice / 100;

        return total_price_f;
    }

    /**
     * Used to finalize a purchase after scanning one or more items
     * @param bp BillPack to cover purchase
     * @param cp CoinPack to cover purchase
     * @return change to the user as a double
     * @throws IllegalStateException if the purchase fails for any reason
     */
    public double finalizePurchase(BillPack bp, CoinPack cp) {
        // Use purchase item to try to finalize the purchase. Here we treat the full purchase
        // list as if it was a single item for simplicity
        double total_price = (double)this.totalPurchasePrice / 100;

        double change_due = 0.0;
        try {
            change_due = purchaseItem(total_price, bp, cp);
        }
         /*
         ***** BONUS *****
         Decide how you want to handle this type of error, for now it clears the list and
         says too bad
         ***** BONUS *****
        */
        catch(IllegalStateException e){
            this.totalPurchasePrice = 0;
            this.purchasePriceList = new ArrayList<>();
            this.purchaseNameList = new ArrayList<>();
            Util.writeln("Sorry, purchase failed");
            throw new IllegalStateException("Sorry, purchase failed");
        }

        // If the purchase was successful we need to reset the purchase list and the total
        // purchase price tracking variable
        this.totalPurchasePrice = 0;
        this.purchasePriceList = new ArrayList<>();
        this.purchaseNameList = new ArrayList<>();

        return change_due;
    }

    /**
     * Determine the number and which bills are to be returned to the customer as change
     * @param total_change_due total amount of change due to customer, in pennies
     * @return BillPack representing bills due to customer, based on bills contained within Drawer
     */
    private BillPack changeBills(long total_change_due){
        long c_hundred = 0;
        long c_fifty = 0;
        long c_twenty = 0;
        long c_ten = 0;
        long c_five = 0;
        long c_one = 0;

        // Cut off the coin part of the change and just get a dollar value
        long total_change = total_change_due / 100;

        if(total_change >= 100) {
            c_hundred = total_change / 100;
            if (c_hundred > drawer.hundred()) c_hundred = drawer.hundred();
            total_change -= (c_hundred * 100);
        }

        if(total_change >= 50) {
            c_fifty = total_change / 50;
            if (c_fifty > drawer.fifty()) c_fifty = drawer.fifty();
            total_change -= (c_fifty * 50);
        }

        if(total_change >= 20){
            c_twenty = total_change / 20;
            if(c_twenty > drawer.twenty()) c_twenty = drawer.twenty();
            total_change -= (c_twenty * 20);
        }

        if(total_change >= 10){
            c_ten = total_change / 10;
            if(c_ten > drawer.ten()) c_ten = drawer.ten();
            total_change -= (c_ten * 10);
        }

        if(total_change >= 5){
            c_five = total_change / 5;
            if(c_five > drawer.five()) c_five = drawer.five();
            total_change -= (c_five * 5);
        }

        if(total_change >= 1){
            c_one = total_change;
            if(c_one > drawer.one()) c_one = drawer.one();
        }

        return new BillPack(c_one, c_five, c_ten, c_twenty, c_fifty, c_hundred);
    }

    /**
     * Determine the number and which coins are to be returned to the customer as change
     * @param remaining_change_due total amount of change due after calculating bills, in pennies
     * @return CoinPack representing coins due to customer, based on coins contained within Drawer
     */
    private CoinPack changeCoins(long remaining_change_due){
        long c_quarter = 0;
        long c_dime = 0;
        long c_nickle = 0;
        long c_penny = 0;

        if(remaining_change_due >= 25){
            c_quarter = remaining_change_due / 25;
            if(c_quarter > drawer.quarter()) c_quarter = drawer.quarter();
            remaining_change_due -= (c_quarter * 25);
        }

        if(remaining_change_due >= 10){
            c_dime = remaining_change_due / 10;
            if(c_dime > drawer.dime()) c_dime = drawer.dime();
            remaining_change_due -= (c_dime * 10);
        }

        if(remaining_change_due >= 5){
            c_nickle = remaining_change_due / 5;
            if(c_nickle > drawer.nickle()) c_nickle = drawer.nickle();
            remaining_change_due -= (c_nickle * 5);
        }

        if(remaining_change_due >= 1){
            c_penny = remaining_change_due;
            if(c_penny > drawer.penny()) c_penny = drawer.penny();
            remaining_change_due -= c_penny;
        }

        if(remaining_change_due != 0) {
            throw new IllegalStateException("Insufficient coins to make change");
        }

        return new CoinPack(c_penny, c_nickle, c_dime, c_quarter);
    }

    /**
     * Displays change due to user in a beautiful format
     * @param price purchase price, in pennies
     * @param tendered tendered, in pennies
     * @param total_change change due to user, in pennies
     */
    private void displayChange(long price, long tendered, long total_change){
        Util.writeln("\n------------------------------");
        Util.writef("Price: $%.2f\n", (float)price / 100);
        Util.writef("Tax: $%.2f\n", (float)taxAlgo.calculateTax(price) / 100);
        Util.writef("Total: $%.2f\n",(((float)price/100+((float)taxAlgo.calculateTax(price)/100))));
        Util.writef("Tendered: $%.2f\n", (float)tendered / 100);

        Util.writef("Total Change: $%.2f\n", (float)total_change / 100);
        Util.writeln("------------------------------\n");
    }


}
