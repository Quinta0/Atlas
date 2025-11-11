"""
Problem Set 2 - Problem 3
Put Option Analysis
"""

import numpy as np
import matplotlib.pyplot as plt

print("="*80)
print("PROBLEM 3: PUT OPTION ANALYSIS")
print("="*80)
print()

# Given data
amount_eur = 1000  # EUR
option_fee_chf = 75  # CHF
R_3m_EUR = 0.013  # 1.3%
R_3m_CHF = 0.005  # 0.5%
E_spot = 0.95  # CHF/EUR

print("GIVEN INFORMATION:")
print("-" * 80)
print(f"Put option to SELL: {amount_eur:,} EUR")
print(f"Option fee: {option_fee_chf} CHF (paid at signing)")
print(f"3-month EUR interest rate: R_3m_EUR = {R_3m_EUR:.3f} ({R_3m_EUR*100:.1f}%)")
print(f"3-month CHF interest rate: R_3m_CHF = {R_3m_CHF:.3f} ({R_3m_CHF*100:.1f}%)")
print(f"Spot exchange rate: E_CHF/EUR = {E_spot:.2f}")
print()

# Part 1: Calculate expected exchange rate
print("="*80)
print("PART 1: EXPECTED EXCHANGE RATE FROM INTEREST PARITY")
print("="*80)
print()

print("Interest Parity Condition (Uncovered Interest Parity):")
print("  E_e / E_spot = (1 + R_CHF) / (1 + R_EUR)")
print()
print("Solving for expected exchange rate E_e:")
print("  E_e = E_spot × (1 + R_CHF) / (1 + R_EUR)")
print()

E_expected = E_spot * (1 + R_3m_CHF) / (1 + R_3m_EUR)

print(f"Calculation:")
print(f"  E_e = {E_spot:.2f} × (1 + {R_3m_CHF:.3f}) / (1 + {R_3m_EUR:.3f})")
print(f"  E_e = {E_spot:.2f} × {1 + R_3m_CHF:.4f} / {1 + R_3m_EUR:.4f}")
print(f"  E_e = {E_spot:.2f} × {(1 + R_3m_CHF) / (1 + R_3m_EUR):.6f}")
print(f"  E_e = {E_expected:.6f}")
print()

print(f"✓ ANSWER: E_e_CHF/EUR = {E_expected:.4f} CHF per EUR")
print()

print("Interpretation:")
print(f"  • The expected exchange rate ({E_expected:.4f}) is LOWER than spot ({E_spot:.2f})")
print(f"  • This means the CHF is expected to APPRECIATE relative to EUR")
print(f"  • This makes sense: CHF has lower interest rate than EUR")
print(f"  • By interest parity, lower interest rate currency appreciates")
print()

# Strike price equals expected exchange rate
X = E_expected

print(f"Strike Price: X = E_e = {X:.4f} CHF/EUR")
print()

# Part 2: Exercise decision when E = 0.93
print("="*80)
print("PART 2: SCENARIO WITH E_CHF/EUR = 0.93 AFTER 3 MONTHS")
print("="*80)
print()

E_future_1 = 0.93

print(f"After 3 months: E_CHF/EUR = {E_future_1:.2f}")
print(f"Strike price: X = {X:.4f}")
print()

print("EXERCISE DECISION:")
print("-" * 80)
print()
print("Put option gives the RIGHT (not obligation) to SELL EUR at strike price X")
print()
print(f"  • If we exercise: Sell 1,000 EUR at X = {X:.4f} CHF/EUR")
print(f"    → Receive: {amount_eur:,} × {X:.4f} = {amount_eur * X:.2f} CHF")
print()
print(f"  • If we don't exercise: Sell 1,000 EUR at market rate E = {E_future_1:.2f}")
print(f"    → Receive: {amount_eur:,} × {E_future_1:.2f} = {amount_eur * E_future_1:.2f} CHF")
print()

if X > E_future_1:
    exercise_1 = True
    print(f"Since X ({X:.4f}) > E ({E_future_1:.2f}), we SHOULD EXERCISE the option!")
    print(f"We can sell EUR at a better rate than the market offers.")
else:
    exercise_1 = False
    print(f"Since X ({X:.4f}) ≤ E ({E_future_1:.2f}), we should NOT exercise.")
    print(f"The market rate is better than the strike price.")
print()

print("PAYOFF AND PROFIT:")
print("-" * 80)
print()

if exercise_1:
    payoff_1 = amount_eur * (X - E_future_1)
    print("Payoff (intrinsic value at expiration):")
    print(f"  Payoff = Amount × max(X - E, 0)")
    print(f"  Payoff = {amount_eur:,} × max({X:.4f} - {E_future_1:.2f}, 0)")
    print(f"  Payoff = {amount_eur:,} × {X - E_future_1:.4f}")
    print(f"  Payoff = {payoff_1:.2f} CHF")
else:
    payoff_1 = 0
    print("Payoff (intrinsic value at expiration):")
    print(f"  Payoff = Amount × max(X - E, 0)")
    print(f"  Payoff = {amount_eur:,} × max({X:.4f} - {E_future_1:.2f}, 0)")
    print(f"  Payoff = 0 CHF (option expires worthless)")

print()

# Calculate profit (accounting for option premium with interest)
option_cost_future = option_fee_chf * (1 + R_3m_CHF)
profit_1 = payoff_1 - option_cost_future

print("Profit (payoff minus cost of option with interest):")
print(f"  Option fee paid upfront: {option_fee_chf} CHF")
print(f"  Future value of option fee: {option_fee_chf} × (1 + {R_3m_CHF:.3f}) = {option_cost_future:.2f} CHF")
print(f"  Profit = Payoff - FV(Option Fee)")
print(f"  Profit = {payoff_1:.2f} - {option_cost_future:.2f}")
print(f"  Profit = {profit_1:.2f} CHF")
print()

if profit_1 > 0:
    print(f"✓ The option generates a POSITIVE profit of {profit_1:.2f} CHF")
elif profit_1 < 0:
    print(f"✗ The option generates a NEGATIVE profit (loss) of {abs(profit_1):.2f} CHF")
else:
    print("○ The option breaks even (zero profit)")
print()

print(f"✓ ANSWER PART 2:")
print(f"  • Exercise decision: {'YES, exercise the option' if exercise_1 else 'NO, let it expire'}")
print(f"  • Payoff: {payoff_1:.2f} CHF")
print(f"  • Profit: {profit_1:.2f} CHF")
print()

# Part 3: Exercise decision when E = 0.98
print("="*80)
print("PART 3: SCENARIO WITH E_CHF/EUR = 0.98 AFTER 3 MONTHS")
print("="*80)
print()

E_future_2 = 0.98

print(f"After 3 months: E_CHF/EUR = {E_future_2:.2f}")
print(f"Strike price: X = {X:.4f}")
print()

print("EXERCISE DECISION:")
print("-" * 80)
print()
print("Put option gives the RIGHT (not obligation) to SELL EUR at strike price X")
print()
print(f"  • If we exercise: Sell 1,000 EUR at X = {X:.4f} CHF/EUR")
print(f"    → Receive: {amount_eur:,} × {X:.4f} = {amount_eur * X:.2f} CHF")
print()
print(f"  • If we don't exercise: Sell 1,000 EUR at market rate E = {E_future_2:.2f}")
print(f"    → Receive: {amount_eur:,} × {E_future_2:.2f} = {amount_eur * E_future_2:.2f} CHF")
print()

if X > E_future_2:
    exercise_2 = True
    print(f"Since X ({X:.4f}) > E ({E_future_2:.2f}), we SHOULD EXERCISE the option!")
    print(f"We can sell EUR at a better rate than the market offers.")
else:
    exercise_2 = False
    print(f"Since X ({X:.4f}) ≤ E ({E_future_2:.2f}), we should NOT exercise.")
    print(f"The market rate is better than the strike price.")
print()

print("PAYOFF AND PROFIT:")
print("-" * 80)
print()

if exercise_2:
    payoff_2 = amount_eur * (X - E_future_2)
    print("Payoff (intrinsic value at expiration):")
    print(f"  Payoff = Amount × max(X - E, 0)")
    print(f"  Payoff = {amount_eur:,} × max({X:.4f} - {E_future_2:.2f}, 0)")
    print(f"  Payoff = {amount_eur:,} × {X - E_future_2:.4f}")
    print(f"  Payoff = {payoff_2:.2f} CHF")
else:
    payoff_2 = 0
    print("Payoff (intrinsic value at expiration):")
    print(f"  Payoff = Amount × max(X - E, 0)")
    print(f"  Payoff = {amount_eur:,} × max({X:.4f} - {E_future_2:.2f}, 0)")
    print(f"  Payoff = 0 CHF (option expires worthless)")

print()

profit_2 = payoff_2 - option_cost_future

print("Profit (payoff minus cost of option with interest):")
print(f"  Option fee paid upfront: {option_fee_chf} CHF")
print(f"  Future value of option fee: {option_fee_chf} × (1 + {R_3m_CHF:.3f}) = {option_cost_future:.2f} CHF")
print(f"  Profit = Payoff - FV(Option Fee)")
print(f"  Profit = {payoff_2:.2f} - {option_cost_future:.2f}")
print(f"  Profit = {profit_2:.2f} CHF")
print()

if profit_2 > 0:
    print(f"✓ The option generates a POSITIVE profit of {profit_2:.2f} CHF")
elif profit_2 < 0:
    print(f"✗ The option generates a NEGATIVE profit (loss) of {abs(profit_2):.2f} CHF")
else:
    print("○ The option breaks even (zero profit)")
print()

print(f"✓ ANSWER PART 3:")
print(f"  • Exercise decision: {'YES, exercise the option' if exercise_2 else 'NO, let it expire'}")
print(f"  • Payoff: {payoff_2:.2f} CHF")
print(f"  • Profit: {profit_2:.2f} CHF")
print()

# Create graphs
print("="*80)
print("GENERATING PAYOFF AND PROFIT DIAGRAMS")
print("="*80)
print()

# Generate exchange rate range
E_range = np.linspace(0.85, 1.05, 200)

# Calculate payoff and profit for each exchange rate
payoffs = amount_eur * np.maximum(X - E_range, 0)
profits = payoffs - option_cost_future

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot 1: Payoff diagram
ax1.plot(E_range, payoffs, 'b-', linewidth=2.5, label='Payoff')
ax1.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax1.axvline(x=X, color='r', linestyle='--', linewidth=1.5, alpha=0.7, label=f'Strike Price (X = {X:.4f})')

# Mark the two scenarios on payoff diagram
ax1.plot(E_future_1, payoff_1, 'go', markersize=12, label=f'Scenario 1: E = {E_future_1:.2f}', zorder=5)
ax1.plot(E_future_2, payoff_2, 'mo', markersize=12, label=f'Scenario 2: E = {E_future_2:.2f}', zorder=5)

# Add annotations
ax1.annotate(f'Payoff = {payoff_1:.2f} CHF', 
             xy=(E_future_1, payoff_1), xytext=(E_future_1-0.03, payoff_1+50),
             fontsize=10, ha='right',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='green', alpha=0.3),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', color='green'))

ax1.annotate(f'Payoff = {payoff_2:.2f} CHF', 
             xy=(E_future_2, payoff_2), xytext=(E_future_2+0.03, payoff_2+50),
             fontsize=10, ha='left',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='magenta', alpha=0.3),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', color='magenta'))

ax1.set_xlabel('Spot Exchange Rate at Maturity (E_CHF/EUR)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Payoff (CHF)', fontsize=11, fontweight='bold')
ax1.set_title('Put Option PAYOFF Diagram\n(Intrinsic Value at Expiration)', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper right', fontsize=10)
ax1.set_xlim([0.85, 1.05])

# Plot 2: Profit diagram
ax2.plot(E_range, profits, 'r-', linewidth=2.5, label='Profit')
ax2.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax2.axvline(x=X, color='r', linestyle='--', linewidth=1.5, alpha=0.7, label=f'Strike Price (X = {X:.4f})')
ax2.axhline(y=-option_cost_future, color='orange', linestyle=':', linewidth=2, 
            label=f'Maximum Loss = -{option_cost_future:.2f} CHF')

# Mark the two scenarios on profit diagram
ax2.plot(E_future_1, profit_1, 'go', markersize=12, label=f'Scenario 1: E = {E_future_1:.2f}', zorder=5)
ax2.plot(E_future_2, profit_2, 'mo', markersize=12, label=f'Scenario 2: E = {E_future_2:.2f}', zorder=5)

# Add annotations
ax2.annotate(f'Profit = {profit_1:.2f} CHF', 
             xy=(E_future_1, profit_1), xytext=(E_future_1-0.03, profit_1+20),
             fontsize=10, ha='right',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='green', alpha=0.3),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', color='green'))

ax2.annotate(f'Profit = {profit_2:.2f} CHF', 
             xy=(E_future_2, profit_2), xytext=(E_future_2+0.03, profit_2-30),
             fontsize=10, ha='left',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='magenta', alpha=0.3),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', color='magenta'))

ax2.set_xlabel('Spot Exchange Rate at Maturity (E_CHF/EUR)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Profit (CHF)', fontsize=11, fontweight='bold')
ax2.set_title('Put Option PROFIT Diagram\n(Payoff - Cost of Option)', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(loc='upper right', fontsize=10)
ax2.set_xlim([0.85, 1.05])

plt.tight_layout()
plt.savefig('/home/quinta/Documents/Atlas/Global Business Environment /Problem Set 2/problem3_put_option_diagrams.png', 
            dpi=300, bbox_inches='tight')
print("✓ Graphs saved as 'problem3_put_option_diagrams.png'")
plt.show()

print()
print("="*80)
print("SUMMARY OF ALL ANSWERS")
print("="*80)
print()
print(f"PART 1: Expected Exchange Rate")
print(f"  E_e_CHF/EUR = {E_expected:.4f}")
print()
print(f"PART 2: Scenario E = {E_future_1:.2f}")
print(f"  • Exercise: {'YES' if exercise_1 else 'NO'}")
print(f"  • Payoff: {payoff_1:.2f} CHF")
print(f"  • Profit: {profit_1:.2f} CHF")
print()
print(f"PART 3: Scenario E = {E_future_2:.2f}")
print(f"  • Exercise: {'YES' if exercise_2 else 'NO'}")
print(f"  • Payoff: {payoff_2:.2f} CHF")
print(f"  • Profit: {profit_2:.2f} CHF")
print()
print("="*80)
