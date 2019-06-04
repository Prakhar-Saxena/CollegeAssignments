/**
 * @author Sean Grimes, 09/19/17
 * <p>
 * CoinPack is a simple container class to hold the 4 (common) types of coins used in US currency.
 * </p>
 * <p><b>
 * NOTE: This is a dumb container to simplify moving coins around between objects, there is little
 * in the way of error checking logic. It's expected that objects using a CoinPack will provide
 * the error checking logic.
 * </b></p>
 */
public class CoinPack {
    long[] cents;

    /**
     * Default c'tor, sets all coin values to zero
     */
    public CoinPack(){
        cents = new long[4];
    }

    /**
     * Instantiate a CoinPack with the number of each type of coin
     * @param penny number of pennies
     * @param nickle number of nickles
     * @param dime number of dimes
     * @param quarter number of quarters
     */
    public CoinPack(long penny, long nickle, long dime, long quarter){
        if(penny < 0 || nickle < 0 || dime < 0 || quarter < 0)
            throw new IllegalArgumentException("Can't store negative coins");
        cents = new long[4];
        cents[0] = penny;
        cents[1] = nickle;
        cents[2] = dime;
        cents[3] = quarter;
    }

    /*
        Getter functions.
        NOTE: These are to be used to determine the number of coins the CoinPack contains, not to
        remove coins from the CoinPack
     */
    public long pennies(){ return cents[0]; }
    public long nickles(){ return cents[1]; }
    public long dimes(){ return cents[2]; }
    public long quarters(){ return cents[3]; }

    /*
        Setter functions.
        These can be used to set a value for each type of coin.
        Returns true when the value is greater than 0, otherwise false.
     */
    public boolean pennies(long penny){
        if(penny < 0) return false;
        cents[0] = (penny);// BUG: cents[0] = (penny + 5);
        return true;
    }

    public boolean nickles(long nickle){
        if(nickle < 0) return false;
        cents[1] = nickle;
        return true;
    }

    public boolean dimes(long dime){
        if(dime < 0) return false;
        cents[2] = dime;
        return true;
    }

    public boolean quarters(long quarter){
        if(quarter < 0) return false;
        cents[3] = quarter;
        return true;
    }
}
