import org.junit.Test;

import static org.junit.Assert.*;

public class CoinPackTest {
    CoinPack coinPack = new CoinPack(1,2,3,4);

    @Test
    public void CoinPackConstructor(){
        CoinPack c = new CoinPack();
        CoinPack newCoinPack = new CoinPack(4,3,2,1);
        assertTrue(newCoinPack.pennies() == 4);
        assertTrue(newCoinPack.nickles() == 3);
        assertTrue(newCoinPack.dimes() == 2);
        assertTrue(newCoinPack.quarters() == 1);
    }

    @Test
    public void pennies() {
        assertTrue(this.coinPack.pennies() == 1);
        assertTrue(!(this.coinPack.pennies(-5)));
        assertTrue(this.coinPack.pennies(5));
        assertTrue(this.coinPack.pennies()==5);
    }

    @Test
    public void nickles() {
        assertTrue(this.coinPack.nickles() == 2);
        assertTrue(!(this.coinPack.nickles(-5)));
        assertTrue(this.coinPack.nickles(5));
        assertTrue(this.coinPack.nickles()==5);
    }

    @Test
    public void dimes() {
        assertTrue(this.coinPack.dimes() == 3);
        assertTrue(!(this.coinPack.dimes(-5)));
        assertTrue(this.coinPack.dimes(5));
        assertTrue(this.coinPack.dimes()==5);
    }

    @Test
    public void quarters() {
        assertTrue(this.coinPack.quarters() == 4);
        assertTrue(!(this.coinPack.quarters(-5)));
        assertTrue(this.coinPack.quarters(5));
        assertTrue(this.coinPack.quarters()==5);
    }
}