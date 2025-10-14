"""
Part 3 Analysis: Twin Deficits Hypothesis
Analyzing the relationship between government budget balance and current account balance
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load the data
ca_data = pd.read_csv('A124RC1A027NBEA.csv')  # Current Account Balance
deficit_data = pd.read_csv('FYFSD.csv')  # Federal Surplus or Deficit
gdp_data = pd.read_csv('FYGDP.csv')  # GDP
private_savings_data = pd.read_csv('W986RC1A027NBEA.csv')  # Net Private Savings
investment_data = pd.read_csv('GPDIA.csv')  # Gross Private Domestic Investment

# Convert dates to datetime
ca_data['observation_date'] = pd.to_datetime(ca_data['observation_date'])
deficit_data['observation_date'] = pd.to_datetime(deficit_data['observation_date'])
gdp_data['observation_date'] = pd.to_datetime(gdp_data['observation_date'])
private_savings_data['observation_date'] = pd.to_datetime(private_savings_data['observation_date'])
investment_data['observation_date'] = pd.to_datetime(investment_data['observation_date'])

# Extract year
ca_data['year'] = ca_data['observation_date'].dt.year
deficit_data['year'] = deficit_data['observation_date'].dt.year
gdp_data['year'] = gdp_data['observation_date'].dt.year
private_savings_data['year'] = private_savings_data['observation_date'].dt.year
investment_data['year'] = investment_data['observation_date'].dt.year

# Filter data from 1960 to 2024
ca_data = ca_data[(ca_data['year'] >= 1960) & (ca_data['year'] <= 2024)]
deficit_data = deficit_data[(deficit_data['year'] >= 1960) & (deficit_data['year'] <= 2024)]
gdp_data = gdp_data[(gdp_data['year'] >= 1960) & (gdp_data['year'] <= 2024)]
private_savings_data = private_savings_data[(private_savings_data['year'] >= 1960) & (private_savings_data['year'] <= 2024)]
investment_data = investment_data[(investment_data['year'] >= 1960) & (investment_data['year'] <= 2024)]

print("="*80)
print("PART 3 ANALYSIS: TWIN DEFICITS HYPOTHESIS")
print("="*80)

# ============================================================================
# QUESTION 1: Government Budget Balance and Current Account Balance
# ============================================================================

print("\n" + "="*80)
print("QUESTION 1: Government Budget Balance vs Current Account Balance")
print("="*80)

# Merge CA and deficit data
merged_data = pd.merge(ca_data[['year', 'A124RC1A027NBEA']], 
                       deficit_data[['year', 'FYFSD']], 
                       on='year', 
                       how='inner')

# Rename columns for clarity
merged_data.columns = ['year', 'CA', 'Sg']

# Convert deficit from millions to billions to match CA
merged_data['Sg'] = merged_data['Sg'] / 1000

print(f"\nData range: {merged_data['year'].min()} to {merged_data['year'].max()}")
print(f"Number of observations: {len(merged_data)}")

# Split data before and after 1990
data_before_1990 = merged_data[merged_data['year'] < 1990]
data_after_1990 = merged_data[merged_data['year'] >= 1990]

# Calculate correlations
corr_before_1990 = data_before_1990['CA'].corr(data_before_1990['Sg'])
corr_after_1990 = data_after_1990['CA'].corr(data_after_1990['Sg'])
corr_overall = merged_data['CA'].corr(merged_data['Sg'])

print(f"\nCorrelation Analysis:")
print(f"  Before 1990 (1960-1989): {corr_before_1990:.4f}")
print(f"  After 1990 (1990-2024):  {corr_after_1990:.4f}")
print(f"  Overall (1960-2024):     {corr_overall:.4f}")

# Statistical significance tests
if len(data_before_1990) > 2:
    corr_before, p_before = stats.pearsonr(data_before_1990['CA'], data_before_1990['Sg'])
    print(f"  Before 1990 p-value: {p_before:.4f}")

if len(data_after_1990) > 2:
    corr_after, p_after = stats.pearsonr(data_after_1990['CA'], data_after_1990['Sg'])
    print(f"  After 1990 p-value: {p_after:.4f}")

# Create visualization for Question 1
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Plot 1: Time series of both variables
ax1 = axes[0]
ax1.plot(merged_data['year'], merged_data['CA'], 'b-', linewidth=2, label='Current Account (CA)')
ax1.plot(merged_data['year'], merged_data['Sg'], 'r-', linewidth=2, label='Government Budget Balance (Sg)')
ax1.axvline(x=1990, color='gray', linestyle='--', linewidth=1.5, label='1990')
ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Billions of Dollars', fontsize=12)
ax1.set_title('US Government Budget Balance and Current Account Balance (1960-2024)', fontsize=14, fontweight='bold')
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Plot 2: Scatter plot
ax2 = axes[1]
ax2.scatter(data_before_1990['Sg'], data_before_1990['CA'], 
           color='blue', alpha=0.6, s=50, label=f'Before 1990 (r={corr_before_1990:.3f})')
ax2.scatter(data_after_1990['Sg'], data_after_1990['CA'], 
           color='red', alpha=0.6, s=50, label=f'After 1990 (r={corr_after_1990:.3f})')

# Add trend lines
z_before = np.polyfit(data_before_1990['Sg'], data_before_1990['CA'], 1)
p_before = np.poly1d(z_before)
z_after = np.polyfit(data_after_1990['Sg'], data_after_1990['CA'], 1)
p_after = np.poly1d(z_after)

sg_range_before = np.linspace(data_before_1990['Sg'].min(), data_before_1990['Sg'].max(), 100)
sg_range_after = np.linspace(data_after_1990['Sg'].min(), data_after_1990['Sg'].max(), 100)

ax2.plot(sg_range_before, p_before(sg_range_before), 'b--', linewidth=2, alpha=0.8)
ax2.plot(sg_range_after, p_after(sg_range_after), 'r--', linewidth=2, alpha=0.8)

ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
ax2.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
ax2.set_xlabel('Government Budget Balance (Sg) - Billions of Dollars', fontsize=12)
ax2.set_ylabel('Current Account (CA) - Billions of Dollars', fontsize=12)
ax2.set_title('Relationship between Government Budget and Current Account', fontsize=14, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('question1_twin_deficits.png', dpi=300, bbox_inches='tight')
print("\n✓ Figure saved as 'question1_twin_deficits.png'")

# ============================================================================
# QUESTION 2: Private Savings and Investment Analysis
# ============================================================================

print("\n" + "="*80)
print("QUESTION 2: Private Savings and Investment Analysis")
print("="*80)

# Merge all data for Question 2
q2_data = pd.merge(private_savings_data[['year', 'W986RC1A027NBEA']], 
                   investment_data[['year', 'GPDIA']], 
                   on='year', 
                   how='inner')
q2_data = pd.merge(q2_data, 
                   gdp_data[['year', 'FYGDP']], 
                   on='year', 
                   how='inner')

# Rename columns
q2_data.columns = ['year', 'Private_Savings', 'Investment', 'GDP']

# Filter for 1960-2024
q2_data = q2_data[(q2_data['year'] >= 1960) & (q2_data['year'] <= 2024)]

# Calculate ratios (as percentages)
q2_data['Savings_GDP_Ratio'] = (q2_data['Private_Savings'] / q2_data['GDP']) * 100
q2_data['Investment_GDP_Ratio'] = (q2_data['Investment'] / q2_data['GDP']) * 100
q2_data['SI_Gap'] = q2_data['Savings_GDP_Ratio'] - q2_data['Investment_GDP_Ratio']

print(f"\nData range: {q2_data['year'].min()} to {q2_data['year'].max()}")
print(f"Number of observations: {len(q2_data)}")

# Summary statistics
print("\nSummary Statistics (% of GDP):")
print("\nBefore 1990:")
before_1990_q2 = q2_data[q2_data['year'] < 1990]
print(f"  Private Savings/GDP: Mean = {before_1990_q2['Savings_GDP_Ratio'].mean():.2f}%, Std = {before_1990_q2['Savings_GDP_Ratio'].std():.2f}%")
print(f"  Investment/GDP:      Mean = {before_1990_q2['Investment_GDP_Ratio'].mean():.2f}%, Std = {before_1990_q2['Investment_GDP_Ratio'].std():.2f}%")
print(f"  S-I Gap:             Mean = {before_1990_q2['SI_Gap'].mean():.2f}%")

print("\nAfter 1990:")
after_1990_q2 = q2_data[q2_data['year'] >= 1990]
print(f"  Private Savings/GDP: Mean = {after_1990_q2['Savings_GDP_Ratio'].mean():.2f}%, Std = {after_1990_q2['Savings_GDP_Ratio'].std():.2f}%")
print(f"  Investment/GDP:      Mean = {after_1990_q2['Investment_GDP_Ratio'].mean():.2f}%, Std = {after_1990_q2['Investment_GDP_Ratio'].std():.2f}%")
print(f"  S-I Gap:             Mean = {after_1990_q2['SI_Gap'].mean():.2f}%")

# Create visualization for Question 2
fig, axes = plt.subplots(3, 1, figsize=(14, 12))

# Plot 1: Private Savings and Investment as % of GDP
ax1 = axes[0]
ax1.plot(q2_data['year'], q2_data['Savings_GDP_Ratio'], 'b-', linewidth=2, label='Private Savings / GDP')
ax1.plot(q2_data['year'], q2_data['Investment_GDP_Ratio'], 'g-', linewidth=2, label='Investment / GDP')
ax1.axvline(x=1990, color='gray', linestyle='--', linewidth=1.5, label='1990')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Percentage of GDP (%)', fontsize=12)
ax1.set_title('Private Savings and Investment as % of GDP (1960-2024)', fontsize=14, fontweight='bold')
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Plot 2: Savings-Investment Gap
ax2 = axes[1]
ax2.plot(q2_data['year'], q2_data['SI_Gap'], 'purple', linewidth=2, label='Savings - Investment Gap')
ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
ax2.axvline(x=1990, color='gray', linestyle='--', linewidth=1.5, label='1990')
ax2.fill_between(q2_data['year'], 0, q2_data['SI_Gap'], 
                  where=(q2_data['SI_Gap'] >= 0), alpha=0.3, color='blue', label='Surplus')
ax2.fill_between(q2_data['year'], 0, q2_data['SI_Gap'], 
                  where=(q2_data['SI_Gap'] < 0), alpha=0.3, color='red', label='Deficit')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Percentage Points', fontsize=12)
ax2.set_title('Private Savings - Investment Gap (% of GDP)', fontsize=14, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

# Plot 3: Absolute values in billions
ax3 = axes[2]
ax3.plot(q2_data['year'], q2_data['Private_Savings'], 'b-', linewidth=2, label='Private Savings')
ax3.plot(q2_data['year'], q2_data['Investment'], 'g-', linewidth=2, label='Investment')
ax3.axvline(x=1990, color='gray', linestyle='--', linewidth=1.5, label='1990')
ax3.set_xlabel('Year', fontsize=12)
ax3.set_ylabel('Billions of Dollars', fontsize=12)
ax3.set_title('Private Savings and Investment - Nominal Values (1960-2024)', fontsize=14, fontweight='bold')
ax3.legend(fontsize=10)
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('question2_savings_investment.png', dpi=300, bbox_inches='tight')
print("\n✓ Figure saved as 'question2_savings_investment.png'")

# ============================================================================
# INTEGRATED ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("INTEGRATED ANALYSIS")
print("="*80)

# Merge CA/Sg data with S/I data
integrated_data = pd.merge(merged_data, q2_data[['year', 'SI_Gap']], on='year', how='inner')

print("\nRelationship between S-I Gap and Current Account:")
corr_si_ca_before = data_before_1990.merge(before_1990_q2[['year', 'SI_Gap']], on='year')['SI_Gap'].corr(
    data_before_1990.merge(before_1990_q2[['year', 'SI_Gap']], on='year')['CA']
)
corr_si_ca_after = data_after_1990.merge(after_1990_q2[['year', 'SI_Gap']], on='year')['SI_Gap'].corr(
    data_after_1990.merge(after_1990_q2[['year', 'SI_Gap']], on='year')['CA']
)

print(f"  Before 1990: r = {corr_si_ca_before:.4f}")
print(f"  After 1990:  r = {corr_si_ca_after:.4f}")

print("\n" + "="*80)
print("INTERPRETATION AND CONCLUSIONS")
print("="*80)

print("""
QUESTION 1 - Twin Deficits Hypothesis:

The twin deficits hypothesis suggests that government budget deficits and current account
deficits move together. The data shows:

Before 1990 (1960-1989):
  - Correlation: {:.4f}
  - The relationship was relatively weak and positive
  - Both CA and Sg were more stable and closer to balance

After 1990 (1990-2024):
  - Correlation: {:.4f}
  - The relationship became much stronger
  - Large structural shifts: persistent CA and government deficits
  - The twin deficits hypothesis appears MORE supported in this period

The data SUPPORTS the twin deficits hypothesis, especially after 1990. The correlation
increased substantially, indicating that as government deficits grew larger (more negative),
current account deficits also grew larger (more negative).

QUESTION 2 - Private Savings and Investment:

Why did the hypothesis strengthen after 1990?

Before 1990:
  - Private Savings/GDP averaged around {:.2f}%
  - Investment/GDP averaged around {:.2f}%
  - S-I gap was relatively small (mean: {:.2f}%)
  - Domestic savings were sufficient to fund domestic investment

After 1990:
  - Private Savings/GDP averaged around {:.2f}%
  - Investment/GDP averaged around {:.2f}%
  - S-I gap increased significantly (mean: {:.2f}%)
  - Private savings DECLINED while investment remained relatively stable
  - This gap needed to be filled by foreign capital (negative CA)

KEY INSIGHT:
The twin deficits hypothesis strengthened after 1990 because:
1. Private savings declined significantly as a share of GDP
2. Investment remained relatively stable
3. With lower private savings, government deficits had a larger impact on national savings
4. The resulting national savings deficit required foreign capital inflows
5. This manifested as persistent current account deficits

The national accounting identity: CA = (S - I) + (T - G)
When private savings (S-I) declined and government deficits (T-G) increased,
the current account (CA) became increasingly negative.
""".format(corr_before_1990, corr_after_1990, 
           before_1990_q2['Savings_GDP_Ratio'].mean(),
           before_1990_q2['Investment_GDP_Ratio'].mean(),
           before_1990_q2['SI_Gap'].mean(),
           after_1990_q2['Savings_GDP_Ratio'].mean(),
           after_1990_q2['Investment_GDP_Ratio'].mean(),
           after_1990_q2['SI_Gap'].mean()))

print("\n" + "="*80)
print("Analysis complete! Check the generated PNG files for visualizations.")
print("="*80)

plt.show()
