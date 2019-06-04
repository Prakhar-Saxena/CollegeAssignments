import org.junit.Test;

import static org.junit.Assert.*;

public class CashRegisterTest {

    @Test
    public void CashRegisterConstructor(){
        CashRegister cr = new CashRegister();

        Drawer dr = new Drawer(1,1,1,1,1,1,1,1,1,1);
        cr = new CashRegister(dr);
        assertTrue(cr.drawerValue() == (1 + 5 + 10 + 20 + 50 + 100 + 0.01 + 0.05 + 0.1 + 0.25));

        cr = new CashRegister(1,1,1,1,1,1,1,1,1,1);
        assertTrue(cr.drawerValue() == (1 + 5 + 10 + 20 + 50 + 100 + 0.01 + 0.05 + 0.1 + 0.25));

        PennsylvaniaTax p = new PennsylvaniaTax();
        cr = new CashRegister(1,1,1,1,1,1,1,1,1,1, p);
        assertTrue(cr.drawerValue() == (1 + 5 + 10 + 20 + 50 + 100 + 0.01 + 0.05 + 0.1 + 0.25));

        CoinPack c = new CoinPack(1,1,1,1);
        BillPack b = new BillPack(1,1,1,1,1,1);
        cr = new CashRegister(b,c);
        assertTrue(cr.drawerValue() == (1 + 5 + 10 + 20 + 50 + 100 + 0.01 + 0.05 + 0.1 + 0.25));

        cr = new CashRegister(b, c, p);
        assertTrue(cr.drawerValue() == (1 + 5 + 10 + 20 + 50 + 100 + 0.01 + 0.05 + 0.1 + 0.25));
    }

    @Test
    public void drawerValue() {
        CashRegister cr = new CashRegister(1,1,1,1,1,1,1,1,1,1);
        assertTrue(cr.drawerValue() == (1 + 5 + 10 + 20 + 50 + 100 + 0.01 + 0.05 + 0.1 + 0.25));
    }

    @Test
    public void coinsInDrawer() {
        CashRegister cr = new CashRegister(1,1,1,1,1,1,1,1,1,1);
        CoinPack c = new CoinPack(1,1,1,1);
        assertTrue(cr.coinsInDrawer().pennies() == c.pennies());
        assertTrue(cr.coinsInDrawer().nickles() == c.nickles());
        assertTrue(cr.coinsInDrawer().dimes() == c.dimes());
        assertTrue(cr.coinsInDrawer().quarters() == c.quarters());
    }

    @Test
    public void billsInDrawer() {
        CashRegister cr = new CashRegister(1,1,1,1,1,1,1,1,1,1);
        BillPack b = new BillPack(1,1,1,1,1,1);
        assertTrue(cr.billsInDrawer().ones() == b.ones());
        assertTrue(cr.billsInDrawer().fives() == b.fives());
        assertTrue(cr.billsInDrawer().tens() == b.tens());
        assertTrue(cr.billsInDrawer().twenties() == b.twenties());
        assertTrue(cr.billsInDrawer().fifties() == b.fifties());
        assertTrue(cr.billsInDrawer().hundreds() == b.hundreds());
    }

    @Test
    public void purchaseItem() {
        CashRegister cr = new CashRegister(10,10,10,10,10,10,10,10,10,10);
        BillPack b = new BillPack(1,1,0,0,0,1);
        CoinPack c = new CoinPack(0,0,0,0);
        assertTrue(cr.purchaseItem(100, b,c) == 0);

        cr = new CashRegister(10,10,10,10,10,10,10,10,10,10);
        b = new BillPack(1,1,1,1,1,1);
        c = new CoinPack(1,1,1,1);
        assertTrue(cr.purchaseItem(100, b,c) == (50 + 20 + 10 + 0.25 + 0.1 + 0.05 + 0.01));

        cr = new CashRegister(10,10,10,10,10,10,10,10,10,10);
        assertTrue(cr.purchaseItem(100,1,1,0,0,0,1,0,0,0,0) == 0);

        cr = new CashRegister(10,10,10,10,10,10,10,10,10,10);
        assertTrue(cr.purchaseItem(100,1,1,1,1,1,1,1,1,1,1) == (50 + 20 + 10 + 0.25 + 0.1 + 0.05 + 0.01));
    }

    @Test
    public void scanItem() {
        CashRegister cr = new CashRegister(10,10,10,10,10,10,10,10,10,10);
        assertTrue(cr.scanItem(100,"item1") == 100);
        assertTrue(cr.scanItem(100,"item2") == 200);
    }

    @Test
    public void finalizePurchase() {
        CashRegister cr = new CashRegister(10,10,10,10,10,10,10,10,10,10);
        cr.scanItem(100,"item1");
        cr.scanItem(100,"item2");
        BillPack b = new BillPack(2,1,1,1,1,2);
        CoinPack c = new CoinPack(1,1,1,1);
        assertTrue(cr.finalizePurchase(b,c) == (50 + 20 + 5 + 0.25 + 0.1 + 0.05 + 0.01));
    }

    @Test
    public void changeBills(){
        CashRegister cr = new CashRegister(10,10,10,10,10,10,10,10,10,10);
    }

    @Test
    public void changeCoins(){

    }


}