# Quick Reference Guide - Problem Set 2

## Running the Solutions

### Option 1: Run All Problems
```bash
python run_all_problems.py
```

### Option 2: Run Individual Problems
```bash
python problem1_part1_analysis.py    # Problem 1, Part 1
python problem1_part2_switzerland.py # Problem 1, Part 2 (requires internet)
python problem2_forward_rate.py      # Problem 2
python problem3_put_option.py        # Problem 3
python problem4_money_demand.py      # Problem 4
```

---

## Quick Answer Reference

### Problem 1: Exchange Rates
- **Part 1:** Yen is riskier (amplifies portfolio risk)
- **Part 2:** CHF fixed to USD during Bretton Woods (1944-1973)

### Problem 2: Forward Exchange Rate
- **F_1y_USD/EUR:** 0.9982
- **Movement:** USD depreciates 2.43%
- **R_1y_EUR:** 2.51%

### Problem 3: Put Option
- **E_e:** 0.9425 CHF/EUR
- **E = 0.93:** Exercise, Payoff = 12.50, Profit = -62.88
- **E = 0.98:** Don't exercise, Payoff = 0, Profit = -75.37

### Problem 4: Money Demand
1. **R_CHF:** 1.0%
2. **E_CHF/EUR:** 1.058
3. **Expected movement:** CHF depreciates 4.00%
4. **See diagrams**
5. **New equilibrium:** R_1 = 4.0%, E_1 = 1.089
6. **See diagrams**
7. **M^s,1:** 350 (no change in R or E with accommodation)

---

## Key Formulas

### Exchange Rates
```
Forward Rate: F = E + (Points/10,000)
CIP: F/E = (1 + R_domestic)/(1 + R_foreign)
UIP: E_e/E = (1 + R_domestic)/(1 + R_foreign)
```

### Money Market
```
Equilibrium: M^s/P = L(R,Y)
Problem 4: L = 100 + 1.5×Y - 5000×R
```

### Options
```
Put Payoff: max(X - E, 0) × Amount
Profit: Payoff - Premium × (1 + R)
Exercise: if X > E (strike > spot)
```

---

## Files Generated

### Scripts (6 files)
- `problem1_part1_analysis.py`
- `problem1_part2_switzerland.py`
- `problem2_forward_rate.py`
- `problem3_put_option.py`
- `problem4_money_demand.py`
- `run_all_problems.py`

### Graphics (5 files)
- `switzerland_exchange_rate.png`
- `problem3_put_option_diagrams.png`
- `problem4_part4_initial.png`
- `problem4_part4_no_accommodation.png`
- `problem4_part6_accommodation.png`

### Documentation (3 files)
- `README.md` - Full documentation
- `ANSWER_SUMMARY.md` - Complete solutions
- `QUICK_REFERENCE.md` - This file

---

## Installation

```bash
# Install required packages
pip install pandas matplotlib requests numpy

# Or if using the virtual environment
.venv/bin/pip install pandas matplotlib requests numpy
```

---

## Problem Breakdown

| Problem | Topic | Points | Key Concepts |
|---------|-------|--------|--------------|
| 1.1 | Risk Analysis | 5 | Portfolio theory, covariance |
| 1.2 | Data Analysis | 8 | Fixed vs floating rates |
| 2 | Forward Rates | 15 | CIP, interest differentials |
| 3 | Options | 20 | Put options, payoff diagrams |
| 4 | Money Demand | 50 | UIP, money market equilibrium |

---

## Common Issues

### Problem 1.2 (FRED Data)
- **Issue:** Can't fetch data
- **Solution:** Check internet connection, FRED may be temporarily down

### Graphics Not Displaying
- **Issue:** Plots don't show
- **Solution:** Files are saved as PNG - view them directly

### Import Errors
- **Issue:** Module not found
- **Solution:** Run `pip install pandas matplotlib requests numpy`

---

## Understanding the Economics

### Why does dollar depreciate in Problem 2?
Higher US interest rates (5%) vs Eurozone (2.51%) → Higher inflation expected → Currency depreciates

### Why not exercise in Problem 3.3?
Market rate (0.98) > Strike (0.9425) → Better to sell at market rate than strike price

### Why does CHF appreciate in Problem 4.5?
Output ↑ → Money demand ↑ → Interest rate ↑ → Capital inflows → Currency appreciates

### Why no change in Problem 4.7?
Central bank increases money supply → Prevents interest rate from rising → No exchange rate change (via UIP)

---

## Point Distribution

- Problem 1: **13 points** (5 + 8)
- Problem 2: **15 points** (4 + 4 + 4 + 3)
- Problem 3: **20 points** (7 + 7 + 6)
- Problem 4: **50 points** (5 + 5 + 5 + 10 + 10 + 10 + 5)

**Total: 100 points** (some problems labeled with original point values may differ)

---

## Tips for Success

1. **Understand the notation:**
   - E_CHF/EUR = CHF per EUR (direct quote)
   - Higher E = CHF depreciation
   - Lower E = CHF appreciation

2. **Know when to exercise options:**
   - Put: Exercise if Strike > Spot (X > E)
   - Call: Exercise if Spot > Strike (E > X)

3. **Interest parity intuition:**
   - High interest rate → Expected depreciation
   - Compensates investors for currency risk

4. **Money market mechanics:**
   - Output ↑ → Money demand ↑ → Rate ↑
   - Money supply ↑ → Rate ↓
   - Accommodation = keeping rate constant

---

## Getting Help

1. **Read the README.md** for comprehensive documentation
2. **Check ANSWER_SUMMARY.md** for detailed solutions
3. **Review the generated graphs** for visual understanding
4. **Run individual problems** to focus on specific topics

---

*Good luck with your Global Business Environment course!*
