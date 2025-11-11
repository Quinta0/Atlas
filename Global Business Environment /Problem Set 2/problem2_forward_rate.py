"""
Problem Set 2 - Problem 2
Forward Exchange Rate Analysis
"""

print("="*80)
print("PROBLEM 2: FORWARD EXCHANGE RATE ANALYSIS")
print("="*80)
print()

# Given data
spot_rate = 0.9745  # E_USD/EUR
forward_points = 236.60

print("GIVEN INFORMATION:")
print("-" * 80)
print(f"Spot Exchange Rate (E_USD/EUR): {spot_rate}")
print(f"1-Year Forward Points: {forward_points}")
print()

# Part 1: Calculate forward exchange rate
print("="*80)
print("PART 1: CALCULATE FORWARD EXCHANGE RATE")
print("="*80)
print()

print("Forward points are typically quoted in basis points (1/10,000)")
print("Formula: F = E_spot + (Forward Points / 10,000)")
print()

forward_rate = spot_rate + (forward_points / 10000)

print(f"Calculation:")
print(f"F_1y_USD/EUR = {spot_rate} + ({forward_points} / 10,000)")
print(f"F_1y_USD/EUR = {spot_rate} + {forward_points/10000:.4f}")
print(f"F_1y_USD/EUR = {forward_rate:.4f}")
print()

print(f"✓ ANSWER: The 1-year forward rate is F_1y_USD/EUR = {forward_rate:.4f}")
print()

# Part 2: Expected appreciation or depreciation
print("="*80)
print("PART 2: EXPECTED APPRECIATION OR DEPRECIATION")
print("="*80)
print()

print("Comparing spot and forward rates:")
print(f"  • Spot rate:    E_USD/EUR = {spot_rate:.4f} (USD per EUR)")
print(f"  • Forward rate: F_USD/EUR = {forward_rate:.4f} (USD per EUR)")
print()

difference = forward_rate - spot_rate
pct_change = (difference / spot_rate) * 100

print(f"Change: {forward_rate:.4f} - {spot_rate:.4f} = {difference:.4f}")
print(f"Percentage change: {pct_change:.2f}%")
print()

print("Interpretation:")
print(f"  Since F > E (forward rate > spot rate):")
print(f"  • It takes MORE dollars to buy 1 euro in the forward market")
print(f"  • The dollar is expected to DEPRECIATE relative to the euro")
print(f"  • Equivalently, the euro is expected to APPRECIATE relative to the dollar")
print()

print(f"✓ ANSWER: The market expects a DEPRECIATION of the US Dollar")
print(f"          relative to the Euro in one year.")
print(f"          (The dollar loses value; the euro gains value)")
print()

# Part 3: Intuitive explanation
print("="*80)
print("PART 3: INTUITIVE EXPLANATION")
print("="*80)
print()

print("Why does the market expect the dollar to depreciate?")
print()

print("The forward rate reflects INTEREST RATE DIFFERENTIALS between countries.")
print()

print("1. COVERED INTEREST PARITY (CIP):")
print("   The forward rate adjusts to eliminate arbitrage opportunities between")
print("   investing in USD vs EUR after accounting for exchange rate risk.")
print()

print("   Formula: F/E = (1 + R_USD)/(1 + R_EUR)")
print()

print("2. INTERPRETATION:")
print("   Since F > E, we have:")
print(f"   {forward_rate:.4f}/{spot_rate:.4f} = {forward_rate/spot_rate:.4f}")
print()

implied_ratio = forward_rate / spot_rate

print(f"   This means: (1 + R_USD)/(1 + R_EUR) = {implied_ratio:.4f}")
print()

print("   Rearranging: 1 + R_USD = {:.4f} × (1 + R_EUR)".format(implied_ratio))
print()

print("   If the ratio > 1, then R_USD > R_EUR")
print("   → US interest rates are HIGHER than Eurozone interest rates")
print()

print("3. INTUITIVE EXPLANATION:")
print()
print("   • The US has higher interest rates than the Eurozone")
print("   • Higher interest rates typically indicate:")
print("     - Expectations of higher inflation in the US")
print("     - Or tighter monetary policy")
print("     - Or higher risk premium")
print()
print("   • According to Purchasing Power Parity (PPP):")
print("     Higher inflation → Currency depreciation")
print()
print("   • Covered Interest Parity ensures that investors can't arbitrage:")
print("     - The higher US interest rate is offset by expected dollar depreciation")
print("     - This makes USD and EUR investments equally attractive (when hedged)")
print()
print("   • The forward rate builds in this expected depreciation")
print("     - Investors demand more dollars per euro in the forward market")
print("     - This compensates for the expected loss in dollar value")
print()

print(f"✓ ANSWER: The dollar is expected to depreciate because US interest rates")
print(f"          are higher than Eurozone rates. The interest rate differential")
print(f"          typically reflects inflation differentials or other economic factors")
print(f"          that lead to currency depreciation. The forward premium on the euro")
print(f"          compensates investors for the higher return on dollar-denominated")
print(f"          assets, maintaining covered interest parity.")
print()

# Part 4: Find EUR interest rate
print("="*80)
print("PART 4: FIND R_EUR USING COVERED INTEREST PARITY")
print("="*80)
print()

R_USD = 0.05

print(f"Given: R_1y_USD = {R_USD:.4f} (5%)")
print(f"       E_USD/EUR = {spot_rate:.4f}")
print(f"       F_1y_USD/EUR = {forward_rate:.4f}")
print()

print("Covered Interest Parity Condition:")
print("  F/E = (1 + R_USD)/(1 + R_EUR)")
print()

print("Solving for R_EUR:")
print("  1 + R_EUR = (1 + R_USD) × (E/F)")
print("  R_EUR = (1 + R_USD) × (E/F) - 1")
print()

R_EUR = (1 + R_USD) * (spot_rate / forward_rate) - 1

print(f"Calculation:")
print(f"  R_EUR = (1 + {R_USD}) × ({spot_rate:.4f}/{forward_rate:.4f}) - 1")
print(f"  R_EUR = {1 + R_USD:.4f} × {spot_rate/forward_rate:.6f} - 1")
print(f"  R_EUR = {(1 + R_USD) * (spot_rate / forward_rate):.6f} - 1")
print(f"  R_EUR = {R_EUR:.6f}")
print()

R_EUR_pct = R_EUR * 100

print(f"✓ ANSWER: R_1y_EUR = {R_EUR:.4f} or {R_EUR_pct:.2f}%")
print()

# Verification
print("VERIFICATION:")
print("Checking covered interest parity:")
print()

lhs = forward_rate / spot_rate
rhs = (1 + R_USD) / (1 + R_EUR)

print(f"  Left side:  F/E = {forward_rate:.4f}/{spot_rate:.4f} = {lhs:.6f}")
print(f"  Right side: (1 + R_USD)/(1 + R_EUR) = {1+R_USD:.4f}/{1+R_EUR:.6f} = {rhs:.6f}")
print()

if abs(lhs - rhs) < 0.0001:
    print("✓ Covered Interest Parity HOLDS! ✓")
else:
    print(f"  Difference: {abs(lhs - rhs):.8f}")
print()

print("="*80)
print("SUMMARY OF ANSWERS")
print("="*80)
print()
print(f"1. Forward Exchange Rate: F_1y_USD/EUR = {forward_rate:.4f}")
print()
print(f"2. Expected Movement: The US Dollar is expected to DEPRECIATE")
print(f"   relative to the Euro by {pct_change:.2f}%")
print()
print(f"3. Intuitive Explanation: Higher US interest rates (compared to")
print(f"   Eurozone) imply expected dollar depreciation. The forward premium")
print(f"   compensates for the interest rate differential via covered interest parity.")
print()
print(f"4. Eurozone Interest Rate: R_1y_EUR = {R_EUR:.4f} ({R_EUR_pct:.2f}%)")
print()

print("="*80)
