"""
Problem Set 2 - Problem 1, Part 2, Question e)
Exchange Rate Analysis: Switzerland (CHF) vs US Dollar (USD)
"""

import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime

# FRED API endpoint for Swiss Franc to USD exchange rate
# FRED series: DEXSZUS (Switzerland / U.S. Foreign Exchange Rate)
# This is Swiss Francs per U.S. Dollar

def fetch_fred_data(series_id):
    """Fetch monthly exchange rate data from FRED"""
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    
    try:
        df = pd.read_csv(url)
        print(f"Columns found: {df.columns.tolist()}")
        print(f"First few rows:\n{df.head()}")
        
        # The first column should be DATE
        date_col = df.columns[0]
        value_col = df.columns[1]
        
        df = df.rename(columns={date_col: 'DATE', value_col: 'Exchange_Rate'})
        df['DATE'] = pd.to_datetime(df['DATE'])
        
        # Remove missing values (marked as '.')
        df = df[df['Exchange_Rate'] != '.']
        df['Exchange_Rate'] = pd.to_numeric(df['Exchange_Rate'], errors='coerce')
        df = df.dropna()
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        import traceback
        traceback.print_exc()
        return None

def plot_exchange_rate(df, country_name):
    """Plot exchange rate over time"""
    plt.figure(figsize=(14, 8))
    plt.plot(df['DATE'], df['Exchange_Rate'], linewidth=1.5, color='#d62728')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Swiss Francs per US Dollar', fontsize=12)
    plt.title(f'Switzerland (CHF) / US Dollar Exchange Rate\nMonthly Data from FRED', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # Add annotations for key events
    # Euro floor: September 2011 - January 2015 (CHF was pegged at 1.20 per EUR)
    plt.axvline(x=pd.to_datetime('2011-09-06'), color='green', linestyle='--', alpha=0.7, linewidth=2)
    plt.axvline(x=pd.to_datetime('2015-01-15'), color='red', linestyle='--', alpha=0.7, linewidth=2)
    
    plt.text(pd.to_datetime('2011-09-06'), plt.ylim()[1]*0.95, 
             'Euro Floor\nIntroduced\n(Sep 2011)', 
             rotation=0, verticalalignment='top', fontsize=9, color='green')
    plt.text(pd.to_datetime('2015-01-15'), plt.ylim()[1]*0.95, 
             'Euro Floor\nAbandoned\n(Jan 2015)', 
             rotation=0, verticalalignment='top', fontsize=9, color='red')
    
    plt.tight_layout()
    plt.savefig('/home/quinta/Documents/Atlas/Global Business Environment /Problem Set 2/switzerland_exchange_rate.png', dpi=300, bbox_inches='tight')
    print("Plot saved as 'switzerland_exchange_rate.png'")
    plt.show()

def analyze_fixed_periods(df):
    """Analyze periods when the currency might have been fixed"""
    print("\n" + "="*80)
    print("ANALYSIS: When was the Swiss Franc Fixed Relative to the US Dollar?")
    print("="*80)
    
    # Calculate rolling standard deviation to identify stable periods
    df['Rolling_Std'] = df['Exchange_Rate'].rolling(window=12).std()
    
    print("\nKey Observations:")
    print("-" * 80)
    
    # Historical context
    print("\n1. BRETTON WOODS ERA (1944-1973):")
    bretton_woods = df[(df['DATE'] >= '1944-01-01') & (df['DATE'] <= '1973-12-31')]
    if not bretton_woods.empty:
        print(f"   - Period: 1944-1973")
        print(f"   - Average rate: {bretton_woods['Exchange_Rate'].mean():.4f} CHF/USD")
        print(f"   - Standard deviation: {bretton_woods['Exchange_Rate'].std():.4f}")
        print(f"   - The Swiss Franc was part of the Bretton Woods fixed exchange rate system")
        print(f"   - Fixed at 4.375 CHF per USD (1945-1949), then adjusted to ~4.30 (1949-1973)")
    
    print("\n2. POST-BRETTON WOODS FLOATING (1973-2011):")
    floating = df[(df['DATE'] >= '1973-01-01') & (df['DATE'] <= '2011-09-01')]
    if not floating.empty:
        print(f"   - Period: 1973-2011")
        print(f"   - Average rate: {floating['Exchange_Rate'].mean():.4f} CHF/USD")
        print(f"   - Standard deviation: {floating['Exchange_Rate'].std():.4f}")
        print(f"   - Swiss Franc floated freely, showing significant volatility")
    
    print("\n3. EURO FLOOR PERIOD (September 2011 - January 2015):")
    euro_floor = df[(df['DATE'] >= '2011-09-06') & (df['DATE'] <= '2015-01-15')]
    if not euro_floor.empty:
        print(f"   - Period: September 6, 2011 - January 15, 2015")
        print(f"   - Average rate: {euro_floor['Exchange_Rate'].mean():.4f} CHF/USD")
        print(f"   - Standard deviation: {euro_floor['Exchange_Rate'].std():.4f}")
        print(f"   - Swiss National Bank (SNB) set minimum exchange rate of 1.20 CHF per EUR")
        print(f"   - This indirectly affected CHF/USD rate (reduced volatility)")
        print(f"   - Not directly fixed to USD, but to EUR")
    
    print("\n4. POST-EURO FLOOR (January 2015 - Present):")
    post_floor = df[df['DATE'] >= '2015-01-15']
    if not post_floor.empty:
        print(f"   - Period: January 15, 2015 - Present")
        print(f"   - Average rate: {post_floor['Exchange_Rate'].mean():.4f} CHF/USD")
        print(f"   - Standard deviation: {post_floor['Exchange_Rate'].std():.4f}")
        print(f"   - Swiss Franc floats freely again")
        print(f"   - Significant appreciation immediately after floor removal")
    
    print("\n" + "="*80)
    print("CONCLUSION:")
    print("="*80)
    print("""
The Swiss Franc was FIXED relative to the US Dollar during:
1. BRETTON WOODS SYSTEM (1944-1973): Directly fixed to USD
   - Official fixed exchange rate system
   - Rate: approximately 4.30-4.375 CHF per USD

The Swiss Franc was INDIRECTLY STABILIZED (but not fixed to USD) during:
2. EURO FLOOR PERIOD (September 2011 - January 2015): Fixed to EUR, not USD
   - SNB maintained a floor of 1.20 CHF per EUR
   - This reduced CHF/USD volatility but CHF/USD was not directly fixed
   - Abandoned on January 15, 2015 ("Swiss Franc Shock")

Since 1973 (except for the Euro floor period), the Swiss Franc has generally
floated freely against the US Dollar.
    """)
    print("="*80)

def main():
    print("Fetching Swiss Franc exchange rate data from FRED...")
    print("FRED Series: DEXSZUS (Swiss Francs per US Dollar)")
    print("-" * 80)
    
    # Fetch data
    df = fetch_fred_data('DEXSZUS')
    
    if df is not None:
        print(f"\nData retrieved successfully!")
        print(f"Date range: {df['DATE'].min().date()} to {df['DATE'].max().date()}")
        print(f"Number of observations: {len(df)}")
        print(f"\nFirst few observations:")
        print(df.head())
        print(f"\nLast few observations:")
        print(df.tail())
        
        # Analyze fixed periods
        analyze_fixed_periods(df)
        
        # Plot
        print("\nGenerating plot...")
        plot_exchange_rate(df, "Switzerland")
        
        # Summary statistics
        print("\n" + "="*80)
        print("SUMMARY STATISTICS")
        print("="*80)
        print(df['Exchange_Rate'].describe())
        
    else:
        print("Failed to fetch data. Please check your internet connection.")

if __name__ == "__main__":
    main()
