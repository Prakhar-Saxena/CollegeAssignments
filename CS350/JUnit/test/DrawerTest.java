import org.junit.Test;

import static org.junit.Assert.*;

public class DrawerTest {
    BillPack billPack = new BillPack(1,2,3,4,5,6);
    CoinPack coinPack = new CoinPack(1,2,3,4);
    Drawer emptyDrawer;
    Drawer drawer1 = new Drawer(coinPack,billPack);
    Drawer drawer2 = new Drawer(1,2,3,4,1,2,3,4,5,6);

    @Test
    public void DrawerConstructor(){
        Drawer newDrawer1 = new Drawer(coinPack,billPack);
        Drawer newDrawer2 = new Drawer(1,2,3,4,1,2,3,4,5,6);
        assertTrue(newDrawer1.penny() == 1);
        assertTrue(newDrawer1.nickle() == 2);
        assertTrue(newDrawer1.dime() == 3);
        assertTrue(newDrawer1.quarter() == 4);

        assertTrue(newDrawer1.one() == 1);
        assertTrue(newDrawer1.five() == 2);
        assertTrue(newDrawer1.ten() == 3);
        assertTrue(newDrawer1.twenty() == 4);
        assertTrue(newDrawer1.fifty() == 5);
        assertTrue(newDrawer1.hundred() == 6);


        assertTrue(newDrawer2.penny() == 1);
        assertTrue(newDrawer2.nickle() == 2);
        assertTrue(newDrawer2.dime() == 3);
        assertTrue(newDrawer2.quarter() == 4);

        assertTrue(newDrawer2.one() == 1);
        assertTrue(newDrawer2.five() == 2);
        assertTrue(newDrawer2.ten() == 3);
        assertTrue(newDrawer2.twenty() == 4);
        assertTrue(newDrawer2.fifty() == 5);
        assertTrue(newDrawer2.hundred() == 6);
    }

    @Test
    public void drawerTotalInCents() {
        int c = (1*1) + (2*5) + (3*10) + (4*25);
        int b = (1*100) +(2*500) + (3*1000) + (4*2000) + (5*5000) + (6*10000);
        assertTrue(this.drawer1.drawerTotalInCents() == (c+b));
    }

    @Test
    public void penny() {
        assertTrue(drawer1.penny() == 1);
        assertTrue(drawer2.penny() == 1);
    }

    @Test
    public void nickle() {
        assertTrue(drawer1.nickle() == 2);
        assertTrue(drawer2.nickle() == 2);
    }

    @Test
    public void dime() {
        assertTrue(drawer1.dime() == 3);
        assertTrue(drawer2.dime() == 3);
    }

    @Test
    public void quarter() {
        assertTrue(drawer1.quarter() == 4);
        assertTrue(drawer2.quarter() == 4);
    }

    @Test
    public void one() {
        assertTrue(drawer1.one() == 1);
        assertTrue(drawer2.one() == 1);
    }

    @Test
    public void five() {
        assertTrue(drawer1.five() == 2);
        assertTrue(drawer2.five() == 2);
    }

    @Test
    public void ten() {
        assertTrue(drawer1.ten() == 3);
        assertTrue(drawer2.ten() == 3);
    }

    @Test
    public void twenty() {
        assertTrue(drawer1.twenty() == 4);
        assertTrue(drawer2.twenty() == 4);
    }

    @Test
    public void fifty() {
        assertTrue(drawer1.fifty() == 5);
        assertTrue(drawer2.fifty() == 5);
    }

    @Test
    public void hundred() {
        assertTrue(drawer1.hundred() == 6);
        assertTrue(drawer2.hundred() == 6);
    }

    @Test
    public void coinPack() {
        assertTrue(this.drawer1.coinPack() == this.coinPack);
//        assertTrue(this.drawer2.coinPack() == this.coinPack);
    }

    @Test
    public void billPack() {
        assertTrue(this.drawer1.billPack() == this.billPack);
//        assertTrue(this.drawer2.billPack() == this.billPack);
    }

    @Test
    public void depositChange() {
        emptyDrawer = new Drawer();
        emptyDrawer.depositChange(1,1,1,1);
//        Drawer newDrawer2 = new Drawer(1,2,3,4,1,2,3,4,5,6);
        assertTrue(Drawer.centValueFromCoins(emptyDrawer.coinPack()) == (25 + 10 + 5 + 1));

        CoinPack c = new CoinPack(1,1,1,1);
        emptyDrawer = new Drawer();
        emptyDrawer.depositChange(c);
        assertTrue(Drawer.centValueFromCoins(emptyDrawer.coinPack()) == (25 + 10 + 5 + 1));
    }

    @Test
    public void depositBills() {
        emptyDrawer = new Drawer();
        emptyDrawer.depositBills(1,1,1,1,1,1);
        assertTrue(emptyDrawer.one() == 1);
        assertTrue(emptyDrawer.five() == 1);
        assertTrue(emptyDrawer.ten() == 1);
        assertTrue(emptyDrawer.twenty() == 1);
        assertTrue(emptyDrawer.fifty() == 1);
        assertTrue(emptyDrawer.hundred() == 1);

        emptyDrawer = new Drawer();
        BillPack billPack = new BillPack(1,1,1,1,1,1);
        emptyDrawer.depositBills(billPack);
        assertTrue(emptyDrawer.one() == 1);
        assertTrue(emptyDrawer.five() == 1);
        assertTrue(emptyDrawer.ten() == 1);
        assertTrue(emptyDrawer.twenty() == 1);
        assertTrue(emptyDrawer.fifty() == 1);
        assertTrue(emptyDrawer.hundred() == 1);
        assertTrue(Drawer.centValueFromBills(emptyDrawer.billPack()) == (100 + 500 + 1000 + 2000 + 5000 + 10000));
    }

    @Test
    public void removeChange() {
        emptyDrawer = new Drawer(5,5,5,5,5,5,5,5,5,5);
        emptyDrawer.removeChange(1,1,1,1);
        assertTrue(emptyDrawer.penny() == 4);
        assertTrue(emptyDrawer.nickle() == 4);
        assertTrue(emptyDrawer.dime() == 4);
        assertTrue(emptyDrawer.quarter() == 4);

        emptyDrawer = new Drawer(5,5,5,5,5,5,5,5,5,5);
        CoinPack c = new CoinPack(1,1,1,1);
        emptyDrawer.removeChange(c);
        assertTrue(emptyDrawer.penny() == 4);
        assertTrue(emptyDrawer.nickle() == 4);
        assertTrue(emptyDrawer.dime() == 4);
        assertTrue(emptyDrawer.quarter() == 4);
    }

    @Test
    public void removeBills() {
        emptyDrawer = new Drawer(5,5,5,5,5,5,5,5,5,5);
        emptyDrawer.removeBills(1,1,1,1,1,1);
        assertTrue(emptyDrawer.one() == 4);
        assertTrue(emptyDrawer.five() == 4);
        assertTrue(emptyDrawer.ten() == 4);
        assertTrue(emptyDrawer.twenty() == 4);
        assertTrue(emptyDrawer.fifty() == 4);
        assertTrue(emptyDrawer.hundred() == 4);

        emptyDrawer = new Drawer(5,5,5,5,5,5,5,5,5,5);
        BillPack b = new BillPack(1,1,1,1,1,1);
        emptyDrawer.removeBills(b);
        assertTrue(emptyDrawer.one() == 4);
        assertTrue(emptyDrawer.five() == 4);
        assertTrue(emptyDrawer.ten() == 4);
        assertTrue(emptyDrawer.twenty() == 4);
        assertTrue(emptyDrawer.fifty() == 4);
        assertTrue(emptyDrawer.hundred() == 4);
    }

    @Test
    public void centValueFromCoins() {
        CoinPack c = new CoinPack(1,1,1,1);
        assertTrue(Drawer.centValueFromCoins(c) == (1 + 5 + 10 + 25));
        assertTrue(Drawer.centValueFromCoins(1,1,1,1) == (1 + 5 + 10 + 25));
    }

    @Test
    public void centValueFromBills() {
        BillPack b = new BillPack(1,1,1,1,1,1);
        assertTrue(Drawer.centValueFromBills(b) == (100 + 500 + 1000 + 2000 + 5000 + 10000));
        assertTrue(Drawer.centValueFromBills(1,1,1,1,1,1) == (100 + 500 + 1000 + 2000 + 5000 + 10000));
    }
}