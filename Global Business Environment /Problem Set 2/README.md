# Problem Set 2 - Global Business Environment

## Overview

This problem set covers four main topics in international finance:
1. **Exchange Rate Risk Analysis** - Understanding currency risk from a portfolio perspective
2. **Forward Exchange Rates** - Analyzing forward rates and covered interest parity
3. **Put Options** - Currency option valuation and exercise decisions
4. **Money Demand and Exchange Rates** - Analyzing the relationship between money markets and forex markets

## Files in This Problem Set

### Python Scripts

| File | Description |
|------|-------------|
| `problem1_part1_analysis.py` | Problem 1, Part 1: Exchange rate risk analysis for European resident |
| `problem1_part2_switzerland.py` | Problem 1, Part 2: Swiss Franc exchange rate data from FRED |
| `problem2_forward_rate.py` | Problem 2: Forward exchange rate calculations and analysis |
| `problem3_put_option.py` | Problem 3: Put option analysis with payoff diagrams |
| `problem4_money_demand.py` | Problem 4: Domestic money demand and exchange rate equilibrium |
| `run_all_problems.py` | Master script to run all problems sequentially |

### Generated Outputs

- `switzerland_exchange_rate.png` - Historical CHF/USD exchange rate chart
- `problem3_put_option_diagrams.png` - Put option payoff and profit diagrams
- `problem4_part4_initial.png` - Initial money market and forex market equilibrium
- `problem4_part4_no_accommodation.png` - Equilibrium after output shock (no accommodation)
- `problem4_part6_accommodation.png` - Equilibrium with monetary accommodation

## How to Run

### Run All Problems

To run all problems in sequence:

```bash
python run_all_problems.py
```

### Run Individual Problems

You can also run each problem separately:

```bash
# Problem 1, Part 1: Exchange rate risk analysis
python problem1_part1_analysis.py

# Problem 1, Part 2: Swiss exchange rate data
python problem1_part2_switzerland.py

# Problem 2: Forward exchange rate
python problem2_forward_rate.py

# Problem 3: Put option analysis
python problem3_put_option.py

# Problem 4: Money demand
python problem4_money_demand.py
```

## Requirements

### Python Packages

The scripts require the following Python packages:

```bash
pip install pandas matplotlib requests numpy
```

Or install all at once:

```bash
pip install pandas matplotlib requests numpy
```

### Internet Connection

Problem 1, Part 2 requires an internet connection to fetch data from FRED (Federal Reserve Economic Data).

## Problem Summaries

### Problem 1: Exchange Rate Risk (7 points)

**Part 1** (Conceptual Analysis)
- Analyzes which currency (dollar or yen) is riskier for a European resident
- Considers correlation between currency movements and wealth portfolio
- Uses modern portfolio theory concepts

**Part 2** (Empirical Analysis)
- Fetches historical CHF/USD exchange rate data from FRED
- Identifies fixed exchange rate periods
- Analyzes the Bretton Woods system and Euro floor period
- Generates visualization of exchange rate history

### Problem 2: Forward Exchange Rate (15 points)

1. **Calculate forward rate** from spot rate and forward points
2. **Determine expected currency movement** (appreciation/depreciation)
3. **Explain intuition** behind the expected movement
4. **Solve for EUR interest rate** using covered interest parity

**Key Concepts:**
- Forward points and forward exchange rates
- Covered Interest Parity (CIP)
- Interest rate differentials and currency expectations

### Problem 3: Put Option (20 points)

Analyzes a put option to sell 1,000 EUR with:
- Option fee: 75 CHF
- 3-month maturity
- Strike price = expected exchange rate from interest parity

**Three Parts:**
1. **Calculate expected exchange rate** using uncovered interest parity
2. **Scenario 1**: E = 0.93 CHF/EUR at maturity
   - Exercise decision
   - Payoff and profit calculation
3. **Scenario 2**: E = 0.98 CHF/EUR at maturity
   - Exercise decision
   - Payoff and profit calculation

**Outputs:**
- Detailed payoff and profit diagrams
- Visual representation of both scenarios

### Problem 4: Domestic Money Demand (50 points)

Comprehensive analysis of money market equilibrium and exchange rates:

1. **Find equilibrium Swiss interest rate** (R_CHF)
2. **Find equilibrium spot exchange rate** (E_CHF/EUR)
3. **Determine expected currency movement**
4. **Diagram: Temporary output increase** (no monetary accommodation)
5. **Solve new equilibrium** with output increase
6. **Diagram: With monetary accommodation**
7. **Calculate new money supply** needed for accommodation

**Key Concepts:**
- Money market equilibrium
- Uncovered Interest Parity (UIP)
- Relationship between money market and forex market
- Monetary policy accommodation
- Short-run vs. long-run adjustments

**Outputs:**
- Three detailed diagrams showing:
  - Initial equilibrium
  - Effect of output shock without accommodation
  - Effect with monetary accommodation

## Key Economic Concepts

### Exchange Rate Notation

- **E_CHF/EUR**: Swiss Francs per Euro (direct quote from Swiss perspective)
- **E_USD/EUR**: US Dollars per Euro

### Interest Parity Conditions

**Covered Interest Parity (CIP):**
```
F/E = (1 + R_domestic)/(1 + R_foreign)
```

**Uncovered Interest Parity (UIP):**
```
E_expected/E = (1 + R_domestic)/(1 + R_foreign)
```

### Money Market Equilibrium

```
M^s / P = L(R, Y)
```

Where:
- M^s = Nominal money supply
- P = Price level
- L(R, Y) = Real money demand function
- R = Interest rate
- Y = Output/Income

### Put Option Payoff

For a put option to sell foreign currency:
```
Payoff = Amount × max(Strike - Spot, 0)
Profit = Payoff - Future Value of Premium
```

## Understanding the Results

### Problem 1: Key Insight

The **yen is riskier** than the dollar for a European resident because:
- Dollar provides a **hedge** (appreciates when wealth does well)
- Yen **amplifies risk** (dollar depreciates vs yen when wealth does poorly)
- Portfolio risk depends on **covariance**, not just variance

### Problem 2: Key Insight

Forward rate > Spot rate implies:
- **Dollar expected to depreciate** vs Euro
- Reflects **higher US interest rates** than Eurozone
- Covered interest parity ensures no arbitrage

### Problem 3: Key Insight

Put option provides **downside protection**:
- Exercise when CHF strengthens (E falls below strike)
- Let expire when CHF weakens (E rises above strike)
- Maximum loss = option premium (with interest)

### Problem 4: Key Insight

**Without accommodation:**
- Output increase → Money demand increases → Interest rate rises → Currency appreciates

**With accommodation:**
- Central bank increases money supply → Interest rate stays constant → Exchange rate unchanged

## Troubleshooting

### FRED Data Access

If you get an error accessing FRED data:
1. Check your internet connection
2. Verify the FRED website is accessible: https://fred.stlouisfed.org/
3. The script will print diagnostic information if data fetch fails

### Graphics Display

If graphs don't display:
- They are automatically saved as PNG files in the same directory
- You can view them manually even if the display window doesn't open

### Missing Packages

If you get import errors:
```bash
pip install pandas matplotlib requests numpy
```

## Mathematical Formulas

### Forward Points

```
F = E_spot + (Forward Points / 10,000)
```

### Expected Return from Currency

```
Expected Return = (E_expected - E_spot) / E_spot
```

### Money Demand Function (Problem 4)

```
L(R_CHF, Y_CHF) = 100 + 1.5 × Y_CHF - 5000 × R_CHF
```

## Interpreting Diagrams

### Money Market Diagram (Bottom Panel)
- **X-axis**: Real money balances (M/P)
- **Y-axis**: Interest rate (R)
- **Vertical line**: Money supply (M^s/P)
- **Downward-sloping curve**: Money demand (M^d/P)
- **Intersection**: Equilibrium interest rate

### Forex Market Diagram (Top Panel)
- **X-axis**: Domestic interest rate (R_CHF)
- **Y-axis**: Exchange rate (E_CHF/EUR)
- **Downward-sloping curve**: Foreign return curve (FR)
- Reflects UIP condition

## Additional Notes

### Rounding

All numerical results are rounded to 3 decimal places as specified in Problem 4.

### Assumptions

- Perfect capital mobility
- Rational expectations
- No transaction costs
- Prices are sticky in the short run (Problem 4)

## Contact and Support

For questions about the economic concepts or interpretation of results, please refer to:
- Course materials on exchange rate determination
- Textbook chapters on international finance
- Lecture notes on forward markets and options

## License

This problem set is for educational purposes as part of the Global Business Environment course.
