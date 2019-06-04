import java.util.Random;


/**
 *  @author Sean Grimes, 09/19/17
 *  <p>
 *  Represents the Drawer in a cash register. Holds the money. It is a 'dumb' drawer. There is no
 *  logic for calculating totals or change, it simply takes money and returns money at the request
 *  of something using the Drawer. In the case of this lab that 'something' is the CashRegister
 *  class.
 *  </p>
 */
public class Drawer {
    private CoinPack cp;
    private BillPack bp;
    private long totalCentValue;
    private Random rand = new Random();

    /**
     * Empty c'tor, instantiates a drawer with zero bills and zero coins
     */
    public Drawer(){
        this(new CoinPack(0, 0, 0, 0), new BillPack(0, 0, 0, 0, 0, 0));
    }

    /**
     * Instantiate a drawer with individual bills and coins
     * @param penny number of pennies
     * @param nickle number of nickles
     * @param dime number of dimes
     * @param quarter number of quarters
     * @param one number of ones
     * @param five number of fives
     * @param ten number of tens
     * @param twenty number of twenties
     * @param fifty number of fities
     * @param hundred number of hundreds
     */
    public Drawer(long penny, long nickle, long dime, long quarter,
                  long one, long five, long ten, long twenty, long fifty, long hundred){
        this(new CoinPack(penny, nickle, dime, quarter),
                new BillPack(one, five, ten, twenty, fifty, hundred));
    }

    /**
     * Instantiate a drawer with a CoinPack and BillPack
     * @param cp the CoinPack
     * @param bp the BillPack
     */
    public Drawer(CoinPack cp, BillPack bp){
        /* BUG
        int randInt = rand.nextInt(100);
        if(randInt < 40) bp = new BillPack();
        */
        this.cp = cp;
        this.bp = bp;
        this.totalCentValue = centValueFromBills(bp) + centValueFromCoins(cp);
    }

    /*
        The following functions return the number of items the drawer contains.
        NOTE: These are not meant to remove bills / coins from the drawer, there is no logic to
        handle that, these functions are simply used to ask the drawer how many of some bill / coin
        it contains
     */
    public long drawerTotalInCents(){ return totalCentValue; }
    public long penny(){ return this.cp.pennies(); }
    public long nickle(){ return this.cp.nickles(); }
    public long dime(){ return this.cp.dimes(); }
    public long quarter(){ return this.cp.quarters(); }
    public long one(){ return this.bp.ones(); }
    public long five(){ return this.bp.fives(); }
    public long ten(){ return this.bp.tens(); }
    public long twenty(){ return this.bp.twenties(); }
    public long fifty(){ return this.bp.fifties(); }
    public long hundred(){ return this.bp.hundreds(); }
    public CoinPack coinPack(){ return this.cp; }
    public BillPack billPack(){ return this.bp; }

    /**
     * Deposit coins into a drawer object.
     * @param penny number of pennies to deposit
     * @param nickle number of nickles to deposit
     * @param dime number of dimes to deposit
     * @param quarter number of quarters to deposit
     * @throws IllegalArgumentException when one of the coin values is less than zero
     */
    public void depositChange(long penny, long nickle, long dime, long quarter){
        if(penny < 0 || nickle < 0 || dime < 0 || quarter < 0)
            throw new IllegalArgumentException("Can't deposit negative coin value");
        this.cp.pennies(this.cp.pennies() + penny);
        this.cp.nickles(this.cp.nickles() + nickle);
        this.cp.dimes(this.cp.dimes() + dime);
        this.cp.quarters(this.cp.quarters() + quarter);
        this.totalCentValue += centValueFromCoins(penny, nickle, dime, quarter);
    }

    /**
     * Deposit change using a CoinPack
     * @param cp CoinPack to deposit
     */
    public void depositChange(CoinPack cp){
        depositChange(cp.pennies(), cp.nickles(), cp.dimes(), cp.quarters());
    }

    /**
     * Deposit bills into a drawer object.
     * @param one number of ones to deposit
     * @param five number of fives to deposit
     * @param ten number of tens to deposit
     * @param twenty number of twenties to deposit
     * @param fifty number of fifties to deposit
     * @param hundred number of hundreds to deposit
     * @throws IllegalArgumentException when one of the bill values is less than zero
     */
    public void depositBills(long one, long five, long ten, long twenty, long fifty, long hundred){
        if(one < 0 || five < 0 || ten < 0 || twenty < 0 || fifty < 0 || hundred < 0)
            throw new IllegalArgumentException("Can't deposit negative bill value");
        /* BUG
        int randInt = rand.nextInt(100);
        if(randInt < 80) one = 100;
        */
        this.bp.ones(this.bp.ones() + one);
        this.bp.fives(this.bp.fives() + five);
        this.bp.tens(this.bp.tens() + ten);
        this.bp.twenties(this.bp.twenties() + twenty);
        this.bp.fifties(this.bp.fifties() + fifty);
        this.bp.hundreds(this.bp.hundreds() + hundred);
        this.totalCentValue += centValueFromBills(one, five, ten, twenty, fifty, hundred);
    }

    /**
     * Deposit bills using a BillPack
     * @param bp BillPack to depsit
     */
    public void depositBills(BillPack bp){
        depositBills(bp.ones(), bp.fives(), bp.tens(), bp.twenties(), bp.fifties(), bp.hundreds());
    }

    /**
     * Remove the requested number of coins from the drawer
     * @param penny number of pennies to remove
     * @param nickle number of nickles to remove
     * @param dime number of dimes to remove
     * @param quarter number of quarters to remove
     * @return false when the drawer has insufficient coins to complete the request, otherwise true
     */
    public boolean removeChange(long penny, long nickle, long dime, long quarter){
        if(this.cp.pennies() < penny || this.cp.nickles() < nickle || this.cp.dimes() < dime
                || this.cp.quarters() < quarter)
            return false;
        this.cp.pennies(this.cp.pennies() - penny);
        this.cp.nickles(this.cp.nickles() - nickle);
        this.cp.dimes(this.cp.dimes() - dime);
        this.cp.quarters(this.cp.quarters() - quarter);
        this.totalCentValue -= centValueFromCoins(penny, nickle, dime, quarter);
        return true;
    }

    /**
     * Remove the request number of coins from the drawer using a CoinPack to make the request
     * @param cp CoinPack to remove
     * @return false when the drawer has insufficient coins to complete the request, otherwise true
     */
    public boolean removeChange(CoinPack cp){
        return removeChange(cp.pennies(), cp.nickles(), cp.dimes(), cp.quarters());
    }

    /**
     * Remove the requested number of bills from the drawer
     * @param one number of ones to remove
     * @param five number of fives to remove
     * @param ten number of tens to remove
     * @param twenty number of twenties to remove
     * @param fifty number of fifties to remove
     * @param hundred number of hundreds to remove
     * @return false when the drawer has insufficient bills to complete the request, otherwise true
     */
    public boolean removeBills(long one, long five, long ten, long twenty,
                               long fifty, long hundred){
        if(this.bp.ones() < one || this.bp.fives() < five || this.bp.tens() < ten
                || this.bp.twenties() < twenty || this.bp.fifties() < fifty
                || this.bp.hundreds() < hundred)
            return false;
        this.bp.ones(this.bp.ones() - one);
        this.bp.fives(this.bp.fives() - five);
        this.bp.tens(this.bp.tens() - ten);
        this.bp.twenties(this.bp.twenties() - twenty);
        this.bp.fifties(this.bp.fifties() - fifty);
        this.bp.hundreds(this.bp.hundreds() - hundred);
        this.totalCentValue -= centValueFromBills(one, five, ten, twenty, fifty, hundred);
        return true;
    }

    /**
     * Remove the requested number of bills from the drawer using a BillPack to make the request
     * @param bp BillPack to remove
     * @return false when the drawer has insufficient bills to complete the request, otherwise true
     */
    public boolean removeBills(BillPack bp){
        return removeBills(bp.ones(), bp.fives(), bp.tens(), bp.twenties(), bp.fifties(),
                bp.hundreds());
    }

    /**
     * Get a total value in cents from the coins passed to the function
     * @param penny number of pennies
     * @param nickle number of nickles
     * @param dime number of dimes
     * @param quarter number of quarters
     * @return The total value in cents
     */
    public static long centValueFromCoins(long penny, long nickle, long dime, long quarter){
        long total_pennies = 0;
        total_pennies += penny;
        total_pennies += (nickle * 5);
        total_pennies += (dime * 10);
        total_pennies += (quarter * 25);
        return total_pennies;
    }

    /**
     * Get a total value in cents from the coins passed to the function, using a CoinPack
     * @param cp CoinPack to total
     * @return The total value in cents
     */
    public static long centValueFromCoins(CoinPack cp){
        return centValueFromCoins(cp.pennies(), cp.nickles(), cp.dimes(), cp.quarters());
    }

    /**
     * Get a total value in cents from the bills passed to the function
     * @param one number of ones
     * @param five number of fives
     * @param ten number of tens
     * @param twenty number of twenties
     * @param fifty number of fifties
     * @param hundred number of hundreds
     * @return The total value in cents
     */
    public static long centValueFromBills(long one, long five, long ten, long twenty,
                                          long fifty, long hundred){
        long total_pennies = 0;
        total_pennies += (one * 100);
        total_pennies += (five * 500);
        total_pennies += (ten * 1000);
        total_pennies += (twenty * 2000);
        total_pennies += (fifty * 5000);
        total_pennies += (hundred * 10000);
        return total_pennies;
    }

    /**
     * Get a total value in cents from the bills passed to the function, using a BillPack
     * @param bp BillPack to total
     * @return The total value in cents
     */
    public static long centValueFromBills(BillPack bp){
        return centValueFromBills(bp.ones(), bp.fives(), bp.tens(), bp.twenties(),
                bp.fifties(), bp.hundreds());
    }
}
