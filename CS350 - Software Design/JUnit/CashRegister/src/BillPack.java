/**
 * @author Sean Grimes, 09/19/17
 * <p>
 * BillPack is a simple container class to hold the 6 different types of bills used in US currency.
 * </P>
 * <p><b>
 * NOTE: This is a dumb container to simplify moving bills around between objects, there is little
 * in the way of error checking logic. It's expected that objects using a BillPack will provide
 * the error checking logic.
 * </b></p>
 */
public class BillPack {
    long[] bills;

    /**
     * Default c'tor, sets all bill values to zero
     */
    public BillPack(){
        bills = new long[6];
    }

    /**
     * Instantiate a BillPack with the number of each type of bill.
     * @param one number of ones
     * @param five number of fives
     * @param ten number of tens
     * @param twenty number of twenties
     * @param fifty number of fifties
     * @param hundred number of hundreds
     */
    public BillPack(long one, long five, long ten, long twenty, long fifty, long hundred){
        if(one < 0 || five < 0 || ten < 0 || twenty < 0 || fifty < 0 || hundred < 0)
            throw new IllegalArgumentException("Can't store negative bills");
        bills = new long[6];
        bills[0] = one;
        bills[1] = five;
        bills[2] = ten;
        bills[3] = twenty;
        bills[4] = fifty;
        bills[5] = hundred;
    }

    /*
        Getter functions.
        NOTE: These are to be used to determine the number of bills the BillPack contains, not to
        remove bills from the BillPack
     */
    public long ones(){ return bills[0]; }
    public long fives(){ return bills[1]; }
    public long tens(){ return bills[2]; }
    public long twenties(){ return bills[3]; }
    public long fifties(){ return bills[4]; }
    public long hundreds(){ return bills[5]; }

    /*
        Setter functions.
        These can be used to set a value for each type of bill.
        Returns true when the value is greater than 0, otherwise false.
     */
    public boolean ones(long one){
        if(one < 0) return false;
        bills[0] = one;
        return true;
    }

    public boolean fives(long five){
        if(five < 0) return false;
        bills[1] = five;
        return true;
    }

    public boolean tens(long ten){
        if(ten < 0) return false;
        bills[2] = ten;
        return true;
    }

    public boolean twenties(long twenty){
        if(twenty < 0) return false;
        bills[3] = twenty;
        return true;
    }

    public boolean fifties(long fifty){
        if(fifty < 0) return false;
        bills[4] = fifty;
        return true;
    }

    public boolean hundreds(long hundred){
        if(hundred < 0) return false;
        bills[5] = hundred;
        return true;
    }
}
