"""
Problem Set 2 - Problem 4
Domestic Money Demand Analysis
"""

import numpy as np
import matplotlib.pyplot as plt

print("="*80)
print("PROBLEM 4: DOMESTIC MONEY DEMAND ANALYSIS")
print("="*80)
print()

# Given data
R_EUR = 0.05  # German (Eurozone) interest rate
E_e_CHF_EUR = 1.1  # Expected exchange rate CHF/EUR
P_CHF = 1.0  # Swiss price level
P_EUR = 1.0  # German price level
M_s_CHF = 200  # Swiss money supply
Y_CHF = 100  # Swiss output

print("GIVEN INFORMATION:")
print("-" * 80)
print(f"1-year German interest rate: R_EUR = {R_EUR:.3f} ({R_EUR*100:.1f}%)")
print(f"Expected exchange rate: E_e_CHF/EUR = {E_e_CHF_EUR:.1f}")
print(f"Swiss price level: P_CHF = {P_CHF:.2f}")
print(f"German price level: P_EUR = {P_EUR:.2f}")
print(f"Swiss money supply: M^s_CHF = {M_s_CHF:.0f}")
print(f"Swiss output: Y_CHF = {Y_CHF:.0f}")
print()
print("Real money demand function in Switzerland:")
print("  L(R_CHF, Y_CHF) = 100 + 1.5 × Y_CHF - 5000 × R_CHF")
print()

# Part 1: Find equilibrium Swiss interest rate
print("="*80)
print("PART 1: EQUILIBRIUM SWISS INTEREST RATE")
print("="*80)
print()

print("Money market equilibrium condition:")
print("  M^s / P = L(R, Y)")
print("  Real money supply = Real money demand")
print()

real_money_supply = M_s_CHF / P_CHF
print(f"Real money supply:")
print(f"  M^s_CHF / P_CHF = {M_s_CHF:.0f} / {P_CHF:.2f} = {real_money_supply:.3f}")
print()

print("Real money demand:")
print(f"  L(R_CHF, Y_CHF) = 100 + 1.5 × {Y_CHF:.0f} - 5000 × R_CHF")
print(f"  L(R_CHF, Y_CHF) = 100 + {1.5 * Y_CHF:.0f} - 5000 × R_CHF")
print(f"  L(R_CHF, Y_CHF) = {100 + 1.5 * Y_CHF:.0f} - 5000 × R_CHF")
print()

print("Setting M^s/P = L:")
print(f"  {real_money_supply:.3f} = {100 + 1.5 * Y_CHF:.0f} - 5000 × R_CHF")
print()

print("Solving for R_CHF:")
print(f"  5000 × R_CHF = {100 + 1.5 * Y_CHF:.0f} - {real_money_supply:.3f}")
print(f"  5000 × R_CHF = {100 + 1.5 * Y_CHF - real_money_supply:.3f}")

R_CHF = (100 + 1.5 * Y_CHF - real_money_supply) / 5000

print(f"  R_CHF = {100 + 1.5 * Y_CHF - real_money_supply:.3f} / 5000")
print(f"  R_CHF = {R_CHF:.6f}")
print()

print(f"✓ ANSWER: R_CHF = {R_CHF:.3f} or {R_CHF*100:.1f}%")
print()

# Part 2: Find equilibrium spot exchange rate
print("="*80)
print("PART 2: EQUILIBRIUM SPOT EXCHANGE RATE")
print("="*80)
print()

print("We use the Uncovered Interest Parity (UIP) condition:")
print("  (E_e - E) / E = R_EUR - R_CHF")
print()
print("Or equivalently:")
print("  E_e / E = 1 + R_EUR - R_CHF")
print("  E = E_e / (1 + R_EUR - R_CHF)")
print()

print(f"Calculation:")
print(f"  E_CHF/EUR = {E_e_CHF_EUR:.1f} / (1 + {R_EUR:.3f} - {R_CHF:.3f})")
print(f"  E_CHF/EUR = {E_e_CHF_EUR:.1f} / (1 + {R_EUR - R_CHF:.3f})")
print(f"  E_CHF/EUR = {E_e_CHF_EUR:.1f} / {1 + R_EUR - R_CHF:.3f}")

E_CHF_EUR = E_e_CHF_EUR / (1 + R_EUR - R_CHF)

print(f"  E_CHF/EUR = {E_CHF_EUR:.3f}")
print()

print(f"✓ ANSWER: E_CHF/EUR = {E_CHF_EUR:.3f}")
print()

# Part 3: Expected appreciation or depreciation
print("="*80)
print("PART 3: EXPECTED APPRECIATION/DEPRECIATION OF CHF")
print("="*80)
print()

print(f"Current spot rate: E_CHF/EUR = {E_CHF_EUR:.3f}")
print(f"Expected future rate: E_e_CHF/EUR = {E_e_CHF_EUR:.1f}")
print()

expected_change = E_e_CHF_EUR - E_CHF_EUR
pct_change = (expected_change / E_CHF_EUR) * 100

print(f"Expected change: {E_e_CHF_EUR:.1f} - {E_CHF_EUR:.3f} = {expected_change:.3f}")
print(f"Percentage change: {pct_change:.2f}%")
print()

print("Interpretation:")
if expected_change > 0:
    print(f"  Since E_e > E (expected rate > spot rate):")
    print(f"  • It will take MORE CHF to buy 1 EUR in the future")
    print(f"  • The CHF is expected to DEPRECIATE relative to the EUR")
    print(f"  • The EUR is expected to APPRECIATE relative to the CHF")
    appreciation_direction = "DEPRECIATION"
elif expected_change < 0:
    print(f"  Since E_e < E (expected rate < spot rate):")
    print(f"  • It will take FEWER CHF to buy 1 EUR in the future")
    print(f"  • The CHF is expected to APPRECIATE relative to the EUR")
    print(f"  • The EUR is expected to DEPRECIATE relative to the CHF")
    appreciation_direction = "APPRECIATION"
else:
    print(f"  Since E_e = E (expected rate = spot rate):")
    print(f"  • No change expected")
    appreciation_direction = "NO CHANGE"
print()

print(f"✓ ANSWER: The market expects a {appreciation_direction} of the CHF")
print(f"          relative to the EUR by {abs(pct_change):.2f}%")
print()

# Part 4: Temporary increase in output - diagram
print("="*80)
print("PART 4: TEMPORARY INCREASE IN OUTPUT (Y_CHF = 200)")
print("="*80)
print()

Y_1_CHF = 200

print(f"New output level: Y_1_CHF = {Y_1_CHF:.0f}")
print(f"Money supply remains: M^s_CHF = {M_s_CHF:.0f} (central bank does NOT accommodate)")
print(f"Expected exchange rate unchanged: E_e = {E_e_CHF_EUR:.1f} (temporary shock)")
print()

print("Creating diagram...")
print()

# Create figure with money market (bottom) and forex market (top)
fig = plt.figure(figsize=(14, 10))

# Forex market (top)
ax_forex = plt.subplot(2, 1, 1)

# Interest rate range for forex market
R_range_forex = np.linspace(0, 0.10, 100)

# UIP condition: E = E_e / (1 + R_EUR - R_CHF)
E_range_initial = E_e_CHF_EUR / (1 + R_EUR - R_range_forex)

# Plot FR curve (doesn't shift - expected exchange rate unchanged)
ax_forex.plot(R_range_forex * 100, E_range_initial, 'b-', linewidth=2.5, label='FR (Foreign Return)')

# Initial equilibrium
ax_forex.plot(R_CHF * 100, E_CHF_EUR, 'ro', markersize=12, label='Initial Equilibrium', zorder=5)

# Add equilibrium lines
ax_forex.axhline(y=E_CHF_EUR, color='r', linestyle='--', alpha=0.5, linewidth=1)
ax_forex.axvline(x=R_CHF * 100, color='r', linestyle='--', alpha=0.5, linewidth=1)

ax_forex.set_xlabel('Swiss Interest Rate R_CHF (%)', fontsize=11, fontweight='bold')
ax_forex.set_ylabel('Exchange Rate E_CHF/EUR', fontsize=11, fontweight='bold')
ax_forex.set_title('FOREX MARKET\n(Before Change in Output)', fontsize=13, fontweight='bold')
ax_forex.grid(True, alpha=0.3)
ax_forex.legend(loc='upper right', fontsize=10)
ax_forex.set_xlim([0, 10])
ax_forex.set_ylim([0.8, 1.3])

# Add annotations
ax_forex.annotate(f'E₀ = {E_CHF_EUR:.3f}\nR₀ = {R_CHF*100:.1f}%', 
                  xy=(R_CHF * 100, E_CHF_EUR), 
                  xytext=(R_CHF * 100 + 1.5, E_CHF_EUR + 0.05),
                  fontsize=10,
                  bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                  arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

# Money market (bottom)
ax_money = plt.subplot(2, 1, 2)

# Interest rate range for money market
R_range_money = np.linspace(0, 0.10, 100)

# Initial money demand
L_initial = 100 + 1.5 * Y_CHF - 5000 * R_range_money

# Plot money supply (vertical line)
ax_money.axvline(x=real_money_supply, color='g', linewidth=2.5, label=f'M^s/P = {real_money_supply:.0f}')

# Plot initial money demand
ax_money.plot(L_initial, R_range_money * 100, 'b-', linewidth=2.5, label=f'M^d/P (Y={Y_CHF:.0f})')

# Initial equilibrium
ax_money.plot(real_money_supply, R_CHF * 100, 'ro', markersize=12, label='Initial Equilibrium', zorder=5)

ax_money.set_xlabel('Real Money Balances (M/P)', fontsize=11, fontweight='bold')
ax_money.set_ylabel('Swiss Interest Rate R_CHF (%)', fontsize=11, fontweight='bold')
ax_money.set_title('MONEY MARKET\n(Before Change in Output)', fontsize=13, fontweight='bold')
ax_money.grid(True, alpha=0.3)
ax_money.legend(loc='upper right', fontsize=10)
ax_money.set_xlim([0, 400])
ax_money.set_ylim([0, 10])

# Add annotations
ax_money.annotate(f'R₀ = {R_CHF*100:.1f}%\nM/P = {real_money_supply:.0f}', 
                  xy=(real_money_supply, R_CHF * 100), 
                  xytext=(real_money_supply + 30, R_CHF * 100 + 1),
                  fontsize=10,
                  bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                  arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.tight_layout()
plt.savefig('/home/quinta/Documents/Atlas/Global Business Environment /Problem Set 2/problem4_part4_initial.png', 
            dpi=300, bbox_inches='tight')
print("✓ Initial equilibrium diagram saved as 'problem4_part4_initial.png'")

# Now create the diagram AFTER the output increase
print()
print("Creating diagram with output increase...")
print()

# Part 5: Solve for new short-run equilibrium
print("="*80)
print("PART 5: NEW SHORT-RUN EQUILIBRIUM WITH Y_1_CHF = 200")
print("="*80)
print()

print("New money market equilibrium:")
print(f"  M^s / P = L(R_1_CHF, Y_1_CHF)")
print(f"  {real_money_supply:.0f} = 100 + 1.5 × {Y_1_CHF:.0f} - 5000 × R_1_CHF")
print(f"  {real_money_supply:.0f} = 100 + {1.5 * Y_1_CHF:.0f} - 5000 × R_1_CHF")
print(f"  {real_money_supply:.0f} = {100 + 1.5 * Y_1_CHF:.0f} - 5000 × R_1_CHF")
print()

print("Solving for R_1_CHF:")
print(f"  5000 × R_1_CHF = {100 + 1.5 * Y_1_CHF:.0f} - {real_money_supply:.0f}")
print(f"  5000 × R_1_CHF = {100 + 1.5 * Y_1_CHF - real_money_supply:.0f}")

R_1_CHF = (100 + 1.5 * Y_1_CHF - real_money_supply) / 5000

print(f"  R_1_CHF = {100 + 1.5 * Y_1_CHF - real_money_supply:.0f} / 5000")
print(f"  R_1_CHF = {R_1_CHF:.6f}")
print()

print(f"New Swiss interest rate: R_1_CHF = {R_1_CHF:.3f} ({R_1_CHF*100:.1f}%)")
print()

print("New spot exchange rate (using UIP):")
print(f"  E_1_CHF/EUR = E_e / (1 + R_EUR - R_1_CHF)")
print(f"  E_1_CHF/EUR = {E_e_CHF_EUR:.1f} / (1 + {R_EUR:.3f} - {R_1_CHF:.3f})")
print(f"  E_1_CHF/EUR = {E_e_CHF_EUR:.1f} / {1 + R_EUR - R_1_CHF:.3f}")

E_1_CHF_EUR = E_e_CHF_EUR / (1 + R_EUR - R_1_CHF)

print(f"  E_1_CHF/EUR = {E_1_CHF_EUR:.3f}")
print()

print(f"✓ ANSWER:")
print(f"  • New interest rate: R_1_CHF = {R_1_CHF:.3f} ({R_1_CHF*100:.1f}%)")
print(f"  • New spot exchange rate: E_1_CHF/EUR = {E_1_CHF_EUR:.3f}")
print()

change_R = R_1_CHF - R_CHF
change_E = E_1_CHF_EUR - E_CHF_EUR

print(f"Changes from initial equilibrium:")
print(f"  • Interest rate change: {change_R:.3f} ({change_R*100:.1f} percentage points)")
print(f"  • Exchange rate change: {change_E:.3f} ({change_E/E_CHF_EUR*100:.2f}%)")
print()

if change_R > 0:
    print(f"  → Interest rate INCREASED (money demand increased, so rate must rise)")
if change_E < 0:
    print(f"  → CHF APPRECIATED (lower E means fewer CHF per EUR)")
print()

# Create new diagram showing the shift
fig2 = plt.figure(figsize=(14, 10))

# Forex market (top) with shift
ax_forex2 = plt.subplot(2, 1, 1)

# FR curve (unchanged)
ax_forex2.plot(R_range_forex * 100, E_range_initial, 'b-', linewidth=2.5, label='FR (Foreign Return)')

# Initial equilibrium
ax_forex2.plot(R_CHF * 100, E_CHF_EUR, 'ro', markersize=12, label='Initial Equilibrium', zorder=5)

# New equilibrium
ax_forex2.plot(R_1_CHF * 100, E_1_CHF_EUR, 'go', markersize=12, label='New Equilibrium (Y↑)', zorder=5)

# Add equilibrium lines
ax_forex2.axhline(y=E_CHF_EUR, color='r', linestyle='--', alpha=0.3, linewidth=1)
ax_forex2.axvline(x=R_CHF * 100, color='r', linestyle='--', alpha=0.3, linewidth=1)
ax_forex2.axhline(y=E_1_CHF_EUR, color='g', linestyle='--', alpha=0.3, linewidth=1)
ax_forex2.axvline(x=R_1_CHF * 100, color='g', linestyle='--', alpha=0.3, linewidth=1)

# Arrow showing movement
ax_forex2.annotate('', xy=(R_1_CHF * 100, E_1_CHF_EUR), xytext=(R_CHF * 100, E_CHF_EUR),
                   arrowprops=dict(arrowstyle='->', lw=2.5, color='purple'))

ax_forex2.set_xlabel('Swiss Interest Rate R_CHF (%)', fontsize=11, fontweight='bold')
ax_forex2.set_ylabel('Exchange Rate E_CHF/EUR', fontsize=11, fontweight='bold')
ax_forex2.set_title('FOREX MARKET: SHORT-RUN EQUILIBRIUM\n(Temporary Output Increase, No Monetary Accommodation)', 
                    fontsize=13, fontweight='bold')
ax_forex2.grid(True, alpha=0.3)
ax_forex2.legend(loc='upper right', fontsize=10)
ax_forex2.set_xlim([0, 10])
ax_forex2.set_ylim([0.8, 1.3])

# Add annotations
ax_forex2.annotate(f'Initial\nE₀ = {E_CHF_EUR:.3f}\nR₀ = {R_CHF*100:.1f}%', 
                   xy=(R_CHF * 100, E_CHF_EUR), 
                   xytext=(R_CHF * 100 - 2, E_CHF_EUR + 0.08),
                   fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='red', alpha=0.3))

ax_forex2.annotate(f'New\nE₁ = {E_1_CHF_EUR:.3f}\nR₁ = {R_1_CHF*100:.1f}%', 
                   xy=(R_1_CHF * 100, E_1_CHF_EUR), 
                   xytext=(R_1_CHF * 100 + 1, E_1_CHF_EUR - 0.08),
                   fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='green', alpha=0.3))

# Money market (bottom) with shift
ax_money2 = plt.subplot(2, 1, 2)

# New money demand
L_new = 100 + 1.5 * Y_1_CHF - 5000 * R_range_money

# Plot money supply (vertical line - unchanged)
ax_money2.axvline(x=real_money_supply, color='g', linewidth=2.5, label=f'M^s/P = {real_money_supply:.0f}')

# Plot both money demand curves
ax_money2.plot(L_initial, R_range_money * 100, 'b--', linewidth=2, alpha=0.6, label=f'M^d/P (Y₀={Y_CHF:.0f})')
ax_money2.plot(L_new, R_range_money * 100, 'b-', linewidth=2.5, label=f'M^d/P (Y₁={Y_1_CHF:.0f})')

# Equilibria
ax_money2.plot(real_money_supply, R_CHF * 100, 'ro', markersize=12, label='Initial Equilibrium', zorder=5)
ax_money2.plot(real_money_supply, R_1_CHF * 100, 'go', markersize=12, label='New Equilibrium', zorder=5)

# Arrow showing shift
ax_money2.annotate('', xy=(250, 5), xytext=(150, 5),
                   arrowprops=dict(arrowstyle='->', lw=2.5, color='blue'))
ax_money2.text(200, 5.5, 'M^d shifts right\n(Y increases)', fontsize=9, ha='center',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='cyan', alpha=0.3))

ax_money2.set_xlabel('Real Money Balances (M/P)', fontsize=11, fontweight='bold')
ax_money2.set_ylabel('Swiss Interest Rate R_CHF (%)', fontsize=11, fontweight='bold')
ax_money2.set_title('MONEY MARKET: SHORT-RUN EQUILIBRIUM\n(Temporary Output Increase, No Monetary Accommodation)', 
                    fontsize=13, fontweight='bold')
ax_money2.grid(True, alpha=0.3)
ax_money2.legend(loc='upper right', fontsize=10)
ax_money2.set_xlim([0, 500])
ax_money2.set_ylim([0, 10])

# Add annotations
ax_money2.annotate(f'R₀ = {R_CHF*100:.1f}%', 
                   xy=(real_money_supply, R_CHF * 100), 
                   xytext=(real_money_supply + 40, R_CHF * 100),
                   fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='red', alpha=0.3),
                   arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3'))

ax_money2.annotate(f'R₁ = {R_1_CHF*100:.1f}%', 
                   xy=(real_money_supply, R_1_CHF * 100), 
                   xytext=(real_money_supply + 40, R_1_CHF * 100),
                   fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='green', alpha=0.3),
                   arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3'))

plt.tight_layout()
plt.savefig('/home/quinta/Documents/Atlas/Global Business Environment /Problem Set 2/problem4_part4_no_accommodation.png', 
            dpi=300, bbox_inches='tight')
print("✓ Diagram saved as 'problem4_part4_no_accommodation.png'")

# Part 6: With monetary accommodation
print()
print("="*80)
print("PART 6: WITH MONETARY ACCOMMODATION")
print("="*80)
print()

print("If the central bank ACCOMMODATES the change in money demand:")
print("  • Money supply increases to keep interest rate constant")
print("  • R_CHF remains at R₀")
print("  • Exchange rate remains at E₀")
print()

print("Creating diagram with accommodation...")
print()

# Part 7: Calculate new money supply
print("="*80)
print("PART 7: NEW MONEY SUPPLY WITH ACCOMMODATION")
print("="*80)
print()

print("With accommodation, the central bank maintains R_CHF = R₀")
print(f"  R_CHF = {R_CHF:.3f}")
print()

print("New money market equilibrium:")
print(f"  M^s,1 / P = L(R_CHF, Y_1_CHF)")
print(f"  M^s,1 / {P_CHF:.2f} = 100 + 1.5 × {Y_1_CHF:.0f} - 5000 × {R_CHF:.3f}")
print(f"  M^s,1 / {P_CHF:.2f} = 100 + {1.5 * Y_1_CHF:.0f} - {5000 * R_CHF:.0f}")
print(f"  M^s,1 / {P_CHF:.2f} = {100 + 1.5 * Y_1_CHF - 5000 * R_CHF:.0f}")
print()

M_s_1_CHF = (100 + 1.5 * Y_1_CHF - 5000 * R_CHF) * P_CHF

print(f"  M^s,1 = {100 + 1.5 * Y_1_CHF - 5000 * R_CHF:.0f} × {P_CHF:.2f}")
print(f"  M^s,1 = {M_s_1_CHF:.0f}")
print()

print(f"✓ ANSWER: M^s,1_CHF = {M_s_1_CHF:.0f}")
print()

change_M = M_s_1_CHF - M_s_CHF

print(f"Change in money supply: ΔM^s = {M_s_1_CHF:.0f} - {M_s_CHF:.0f} = {change_M:.0f}")
print()

print("Do the spot exchange rate and interest rate change?")
print("  • Interest rate: NO CHANGE (R₁ = R₀ = {:.3f})".format(R_CHF))
print("  • Exchange rate: NO CHANGE (E₁ = E₀ = {:.3f})".format(E_CHF_EUR))
print()
print("  The central bank's monetary accommodation prevents any change in")
print("  the interest rate, which (via UIP) prevents any change in the")
print("  exchange rate.")
print()

# Create diagram with accommodation
fig3 = plt.figure(figsize=(14, 10))

# Forex market (top) - no change
ax_forex3 = plt.subplot(2, 1, 1)

# FR curve
ax_forex3.plot(R_range_forex * 100, E_range_initial, 'b-', linewidth=2.5, label='FR (Foreign Return)')

# Equilibrium (stays the same)
ax_forex3.plot(R_CHF * 100, E_CHF_EUR, 'ro', markersize=12, label='Equilibrium (unchanged)', zorder=5)

# Add equilibrium lines
ax_forex3.axhline(y=E_CHF_EUR, color='r', linestyle='--', alpha=0.5, linewidth=1)
ax_forex3.axvline(x=R_CHF * 100, color='r', linestyle='--', alpha=0.5, linewidth=1)

ax_forex3.set_xlabel('Swiss Interest Rate R_CHF (%)', fontsize=11, fontweight='bold')
ax_forex3.set_ylabel('Exchange Rate E_CHF/EUR', fontsize=11, fontweight='bold')
ax_forex3.set_title('FOREX MARKET: SHORT-RUN EQUILIBRIUM\n(With Monetary Accommodation - No Change)', 
                    fontsize=13, fontweight='bold')
ax_forex3.grid(True, alpha=0.3)
ax_forex3.legend(loc='upper right', fontsize=10)
ax_forex3.set_xlim([0, 10])
ax_forex3.set_ylim([0.8, 1.3])

# Add annotation
ax_forex3.annotate(f'E = {E_CHF_EUR:.3f}\nR = {R_CHF*100:.1f}%\n(UNCHANGED)', 
                   xy=(R_CHF * 100, E_CHF_EUR), 
                   xytext=(R_CHF * 100 + 2, E_CHF_EUR + 0.08),
                   fontsize=10,
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                   arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

# Money market (bottom) - both supply and demand shift
ax_money3 = plt.subplot(2, 1, 2)

new_real_money_supply = M_s_1_CHF / P_CHF

# Plot both money supply lines
ax_money3.axvline(x=real_money_supply, color='g', linestyle='--', linewidth=2, alpha=0.6, 
                  label=f'M^s₀/P = {real_money_supply:.0f}')
ax_money3.axvline(x=new_real_money_supply, color='g', linewidth=2.5, 
                  label=f'M^s₁/P = {new_real_money_supply:.0f}')

# Plot both money demand curves
ax_money3.plot(L_initial, R_range_money * 100, 'b--', linewidth=2, alpha=0.6, label=f'M^d/P (Y₀={Y_CHF:.0f})')
ax_money3.plot(L_new, R_range_money * 100, 'b-', linewidth=2.5, label=f'M^d/P (Y₁={Y_1_CHF:.0f})')

# Equilibria (both at same interest rate)
ax_money3.plot(real_money_supply, R_CHF * 100, 'ro', markersize=10, alpha=0.6, label='Initial Equilibrium', zorder=5)
ax_money3.plot(new_real_money_supply, R_CHF * 100, 'go', markersize=12, label='New Equilibrium', zorder=5)

# Arrows showing shifts
ax_money3.annotate('M^d shifts\nright', xy=(270, 3), xytext=(230, 3.8),
                   arrowprops=dict(arrowstyle='->', lw=2, color='blue'),
                   fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='cyan', alpha=0.3))

ax_money3.annotate('M^s shifts\nright', xy=(300, 7), xytext=(260, 7.8),
                   arrowprops=dict(arrowstyle='->', lw=2, color='green'),
                   fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.3))

ax_money3.set_xlabel('Real Money Balances (M/P)', fontsize=11, fontweight='bold')
ax_money3.set_ylabel('Swiss Interest Rate R_CHF (%)', fontsize=11, fontweight='bold')
ax_money3.set_title('MONEY MARKET: SHORT-RUN EQUILIBRIUM\n(With Monetary Accommodation - Both Curves Shift)', 
                    fontsize=13, fontweight='bold')
ax_money3.grid(True, alpha=0.3)
ax_money3.legend(loc='upper right', fontsize=9)
ax_money3.set_xlim([0, 500])
ax_money3.set_ylim([0, 10])

# Add annotation showing rate stays constant
ax_money3.axhline(y=R_CHF * 100, color='orange', linestyle=':', linewidth=2, alpha=0.7)
ax_money3.text(250, R_CHF * 100 + 0.5, f'R = {R_CHF*100:.1f}% (CONSTANT)', 
               fontsize=10, ha='center',
               bbox=dict(boxstyle='round,pad=0.4', facecolor='orange', alpha=0.5))

plt.tight_layout()
plt.savefig('/home/quinta/Documents/Atlas/Global Business Environment /Problem Set 2/problem4_part6_accommodation.png', 
            dpi=300, bbox_inches='tight')
print("✓ Diagram saved as 'problem4_part6_accommodation.png'")

plt.show()

print()
print("="*80)
print("SUMMARY OF ALL ANSWERS - PROBLEM 4")
print("="*80)
print()
print(f"1. Equilibrium Swiss interest rate: R_CHF = {R_CHF:.3f} ({R_CHF*100:.1f}%)")
print()
print(f"2. Equilibrium spot exchange rate: E_CHF/EUR = {E_CHF_EUR:.3f}")
print()
print(f"3. Expected movement: CHF expected to {appreciation_direction.upper()}")
print(f"   by {abs(pct_change):.2f}% relative to EUR")
print()
print(f"4. Diagram created showing initial equilibrium (see graph)")
print()
print(f"5. New short-run equilibrium (Y₁ = {Y_1_CHF}, no accommodation):")
print(f"   • R_1_CHF = {R_1_CHF:.3f} ({R_1_CHF*100:.1f}%)")
print(f"   • E_1_CHF/EUR = {E_1_CHF_EUR:.3f}")
print(f"   • Interest rate increased by {change_R*100:.1f} percentage points")
print(f"   • CHF appreciated by {abs(change_E/E_CHF_EUR*100):.2f}%")
print()
print(f"6. Diagram created showing equilibrium with no accommodation (see graph)")
print()
print(f"7. New money supply with accommodation: M^s,1_CHF = {M_s_1_CHF:.0f}")
print(f"   • Money supply increases by {change_M:.0f}")
print(f"   • Interest rate: NO CHANGE (R = {R_CHF:.3f})")
print(f"   • Exchange rate: NO CHANGE (E = {E_CHF_EUR:.3f})")
print(f"   • Diagram created (see graph)")
print()
print("="*80)
