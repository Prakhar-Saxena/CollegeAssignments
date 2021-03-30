import org.junit.Test;

import static org.junit.Assert.*;

public class PennsylvaniaTaxTest {

    @Test
    public void calculateTax() {
        PennsylvaniaTax pennsylvaniaTax = new PennsylvaniaTax();
        assertTrue(pennsylvaniaTax.calculateTax(100) == 6);
    }

    @Test
    public void applyTaxToPurchase() {
        PennsylvaniaTax pennsylvaniaTax = new PennsylvaniaTax();
        assertTrue(pennsylvaniaTax.applyTaxToPurchase(100) == 106);
    }
}