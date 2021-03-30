/**
 * @author Sean Grimes, 09/19/17
 * <p>Tax interface, all tax algorithms must implement the below two functions</p>
 */
public interface ITax {
    /**
     * Calculate the amount of tax based on a purchase price
     * @param purchasePrice the purchase price, in pennies
     * @return total tax, in pennies
     */
    long calculateTax(long purchasePrice);

    /**
     * Apply the tax to the total purchase price
     * @param purchasePrice the purchase price, in pennies
     * @return total purchase price, including the tax
     */
    long applyTaxToPurchase(long purchasePrice);
}
