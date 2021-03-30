import org.junit.Test;

import static org.junit.Assert.*;

public class BillPackTest {
    BillPack billPack = new BillPack(1,2,3,4,5,6);

    @Test
    public void BillPackConstructor(){
        BillPack b = new BillPack();
        BillPack newBillPack = new BillPack(6,5,4,3,2,1);
        assertTrue(newBillPack.ones() == 6);
        assertTrue(newBillPack.fives() == 5);
        assertTrue(newBillPack.tens() == 4);
        assertTrue(newBillPack.twenties() == 3);
        assertTrue(newBillPack.fifties() == 2);
        assertTrue(newBillPack.hundreds() == 1);
    }

    @Test
    public void ones() {
        assertTrue(this.billPack.ones() == 1);
        assertTrue(!(this.billPack.ones(-5)));
        assertTrue(this.billPack.ones(5));
        assertTrue(this.billPack.ones() == 5);
    }

    @Test
    public void fives() {
        assertTrue(this.billPack.fives() == 2);
        assertTrue(!(this.billPack.fives(-5)));
        assertTrue(this.billPack.fives(5));
        assertTrue(this.billPack.fives() == 5);
    }

    @Test
    public void tens() {
        assertTrue(this.billPack.tens() == 3);
        assertTrue(!(this.billPack.tens(-5)));
        assertTrue(this.billPack.tens(5));
        assertTrue(this.billPack.tens() == 5);
    }

    @Test
    public void twenties() {
        assertTrue(this.billPack.twenties() == 4);
        assertTrue(!(this.billPack.twenties(-5)));
        assertTrue(this.billPack.twenties(5));
        assertTrue(this.billPack.twenties() == 5);
    }

    @Test
    public void fifties() {
        assertTrue(this.billPack.fifties() == 5);
        assertTrue(!(this.billPack.fifties(-5)));
        assertTrue(this.billPack.fifties(5));
        assertTrue(this.billPack.fifties() == 5);
    }

    @Test
    public void hundreds() {
        assertTrue(this.billPack.hundreds() == 6);
        assertTrue(!(this.billPack.hundreds(-5)));
        assertTrue(this.billPack.hundreds(5));
        assertTrue(this.billPack.hundreds() == 5);
    }
}