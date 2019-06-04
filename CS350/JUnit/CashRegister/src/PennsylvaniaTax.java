/**
 * @author Sean Grimes, 09/19/17
 * <p>The Pennsylvania tax algorithm, implements ITax</p>
 * @see ITax
 */
public class PennsylvaniaTax implements ITax{
    long taxValue = 6;

    @Override
    public long calculateTax(long purchasePrice) {
        return purchasePrice * this.taxValue / 100;
    }

    @Override
    public long applyTaxToPurchase(long purchasePrice) {
        return purchasePrice + calculateTax(purchasePrice);
    }
}
