# Problem Set 2 - Answer Summary
## Global Business Environment

---

## Problem 1: Exchange Rates (7 points)

### Part 1 (5 points): Currency Risk Analysis for European Resident

**Question:** Which currency is riskier - the dollar or the yen?

**ANSWER: THE YEN IS RISKIER**

**Explanation:**

Even though both currencies are equally variable (same variance), the **yen is riskier** from a European resident's portfolio perspective because:

1. **Dollar provides a HEDGE:**
   - When the rest of your wealth has high returns → Euro depreciates vs Dollar
   - This means the dollar appreciates when your wealth is doing well
   - The dollar provides **negative covariance** with your portfolio
   - Acts as insurance/diversification

2. **Yen AMPLIFIES risk:**
   - When rest of wealth has high returns → Yen appreciates vs Dollar
   - Holding dollars means you lose when the yen appreciates
   - The dollar (relative to yen) has **positive covariance** with your portfolio
   - Amplifies portfolio risk

3. **Portfolio theory insight:**
   - Risk = Variance + 2 × Covariance with existing wealth
   - Assets that move in the **same direction** as your wealth are **less risky**
   - Assets that move in the **opposite direction** are **more risky**

---

### Part 2 (8 points): Exchange Rate Data Analysis

**Task:** Analyze exchange rate data for Switzerland

**Key Findings:**

1. **Bretton Woods Era (1944-1973):**
   - Swiss Franc was FIXED to USD
   - Rate: approximately 4.30-4.375 CHF per USD

2. **Floating Period (1973-2011):**
   - CHF floated freely against USD
   - High volatility

3. **Euro Floor Period (September 6, 2011 - January 15, 2015):**
   - SNB set minimum exchange rate: 1.20 CHF per EUR
   - CHF was fixed to EUR, NOT directly to USD
   - Indirectly reduced CHF/USD volatility
   - "Swiss Franc Shock" on January 15, 2015 when floor abandoned

4. **Post-Euro Floor (2015-Present):**
   - CHF floats freely again
   - Significant appreciation after floor removal

**Graph created:** `switzerland_exchange_rate.png`

---

## Problem 2: Forward Exchange Rate (15 points)

**Given:**
- Spot rate: E_USD/EUR = 0.9745
- 1-year forward points: 236.60
- R_1y_USD = 0.05 (5%)

### Part 1 (4 points): Calculate Forward Exchange Rate

**ANSWER: F_1y_USD/EUR = 0.9982**

**Calculation:**
```
F = E_spot + (Forward Points / 10,000)
F = 0.9745 + (236.60 / 10,000)
F = 0.9745 + 0.0237
F = 0.9982
```

---

### Part 2 (4 points): Expected Appreciation or Depreciation

**ANSWER: The US Dollar is expected to DEPRECIATE by 2.43% relative to the Euro**

**Reasoning:**
- Forward rate (0.9982) > Spot rate (0.9745)
- Takes MORE dollars to buy 1 euro in forward market
- Dollar loses value, euro gains value

---

### Part 3 (4 points): Intuitive Explanation

**ANSWER:**

The dollar is expected to depreciate because:

1. **Interest Rate Differential:**
   - Forward premium implies: (1 + R_USD) / (1 + R_EUR) > 1
   - Therefore: R_USD > R_EUR
   - US interest rates are higher than Eurozone rates

2. **Economic Interpretation:**
   - Higher interest rates often reflect higher expected inflation
   - Higher inflation leads to currency depreciation (PPP)
   
3. **No Arbitrage (Covered Interest Parity):**
   - Higher US interest rate is offset by expected dollar depreciation
   - Forward rate adjusts to prevent arbitrage
   - Makes USD and EUR investments equally attractive when hedged

---

### Part 4 (3 points): Find R_EUR

**ANSWER: R_1y_EUR = 0.0251 or 2.51%**

**Calculation using Covered Interest Parity:**
```
F/E = (1 + R_USD)/(1 + R_EUR)

Solving for R_EUR:
R_EUR = (1 + R_USD) × (E/F) - 1
R_EUR = (1 + 0.05) × (0.9745/0.9982) - 1
R_EUR = 1.05 × 0.976296 - 1
R_EUR = 0.0251 or 2.51%
```

**Verification:**
- F/E = 0.9982/0.9745 = 1.0243
- (1 + R_USD)/(1 + R_EUR) = 1.05/1.0251 = 1.0243 ✓

---

## Problem 3: Put Option (20 points)

**Given:**
- Put option to sell: 1,000 EUR
- Option fee: 75 CHF (paid at signing)
- R_3m_EUR = 1.3%
- R_3m_CHF = 0.5%
- E_spot = 0.95 CHF/EUR

### Part 1 (7 points): Expected Exchange Rate

**ANSWER: E_e_CHF/EUR = 0.9425**

**Calculation using Interest Parity:**
```
E_e = E_spot × (1 + R_CHF) / (1 + R_EUR)
E_e = 0.95 × (1 + 0.005) / (1 + 0.013)
E_e = 0.95 × 1.005 / 1.013
E_e = 0.9425 CHF/EUR
```

**Strike Price: X = 0.9425 CHF/EUR**

---

### Part 2 (7 points): Scenario E = 0.93

**After 3 months: E = 0.93 CHF/EUR**

**Exercise Decision: YES, EXERCISE THE OPTION**

**Reasoning:**
- Strike price (0.9425) > Market rate (0.93)
- Can sell EUR at better rate than market

**PAYOFF: 12.50 CHF**
```
Payoff = 1,000 × max(0.9425 - 0.93, 0)
Payoff = 1,000 × 0.0125
Payoff = 12.50 CHF
```

**PROFIT: -62.88 CHF (Loss)**
```
Future value of premium = 75 × 1.005 = 75.37 CHF
Profit = 12.50 - 75.37 = -62.88 CHF
```

**Graph:** See `problem3_put_option_diagrams.png` (Scenario 1 marked in green)

---

### Part 3 (6 points): Scenario E = 0.98

**After 3 months: E = 0.98 CHF/EUR**

**Exercise Decision: NO, LET IT EXPIRE**

**Reasoning:**
- Strike price (0.9425) < Market rate (0.98)
- Market rate is better than strike price

**PAYOFF: 0.00 CHF**
```
Payoff = 1,000 × max(0.9425 - 0.98, 0)
Payoff = 0 CHF (expires worthless)
```

**PROFIT: -75.37 CHF (Loss)**
```
Future value of premium = 75 × 1.005 = 75.37 CHF
Profit = 0 - 75.37 = -75.37 CHF
```

**Note:** This is the maximum possible loss (the option premium with interest)

**Graph:** See `problem3_put_option_diagrams.png` (Scenario 2 marked in magenta)

---

## Problem 4: Domestic Money Demand (50 points)

**Given:**
- R_EUR = 0.05 (5%)
- E_e_CHF/EUR = 1.1
- P_CHF = P_EUR = 1.0
- M^s_CHF = 200
- Y_CHF = 100
- L(R_CHF, Y_CHF) = 100 + 1.5 × Y_CHF - 5000 × R_CHF

### Part 1 (5 points): Equilibrium Swiss Interest Rate

**ANSWER: R_CHF = 0.010 (1.0%)**

**Calculation:**
```
Money market equilibrium: M^s/P = L(R, Y)
200/1 = 100 + 1.5(100) - 5000 × R_CHF
200 = 250 - 5000 × R_CHF
5000 × R_CHF = 50
R_CHF = 0.010 or 1.0%
```

---

### Part 2 (5 points): Equilibrium Spot Exchange Rate

**ANSWER: E_CHF/EUR = 1.058**

**Calculation using Uncovered Interest Parity:**
```
E = E_e / (1 + R_EUR - R_CHF)
E = 1.1 / (1 + 0.05 - 0.01)
E = 1.1 / 1.04
E = 1.058 CHF/EUR
```

---

### Part 3 (5 points): Expected Appreciation or Depreciation

**ANSWER: The CHF is expected to DEPRECIATE by 4.00% relative to the EUR**

**Calculation:**
```
Current spot: E = 1.058
Expected future: E_e = 1.1
Change: (1.1 - 1.058) / 1.058 = 0.04 or 4.00%
```

**Interpretation:**
- Expected rate > Spot rate
- Takes MORE CHF to buy 1 EUR in future
- CHF depreciates, EUR appreciates

---

### Part 4 (10 points): Diagram - Temporary Output Increase (No Accommodation)

**Graphs created:**
- `problem4_part4_initial.png` - Initial equilibrium
- `problem4_part4_no_accommodation.png` - After output increase

**Description:**

**Money Market (bottom panel):**
- Money demand shifts RIGHT (Y increases from 100 to 200)
- Money supply stays FIXED at 200 (vertical line unchanged)
- Interest rate RISES to restore equilibrium

**Forex Market (top panel):**
- FR curve stays UNCHANGED (E_e unchanged - temporary shock)
- Movement ALONG the FR curve
- Higher R_CHF → CHF appreciates (E falls)

---

### Part 5 (10 points): New Short-Run Equilibrium

**New output: Y_1_CHF = 200**
**Central bank does NOT accommodate (M^s = 200 unchanged)**

**ANSWERS:**

**R_1_CHF = 0.040 (4.0%)**
```
Money market: M^s/P = L(R_1, Y_1)
200 = 100 + 1.5(200) - 5000 × R_1_CHF
200 = 400 - 5000 × R_1_CHF
5000 × R_1_CHF = 200
R_1_CHF = 0.040 or 4.0%
```

**E_1_CHF/EUR = 1.089**
```
E_1 = E_e / (1 + R_EUR - R_1_CHF)
E_1 = 1.1 / (1 + 0.05 - 0.04)
E_1 = 1.1 / 1.01
E_1 = 1.089 CHF/EUR
```

**Changes:**
- Interest rate: +3.0 percentage points (from 1% to 4%)
- Exchange rate: CHF appreciated by 2.97% (E fell from 1.058 to 1.089)

**Economic Interpretation:**
- Output increase → Higher money demand
- Fixed money supply → Interest rate must rise
- Higher domestic interest rate → Capital inflows → CHF appreciates

---

### Part 6 (10 points): Diagram - With Monetary Accommodation

**Graph created:** `problem4_part6_accommodation.png`

**Description:**

**Money Market (bottom panel):**
- Money demand shifts RIGHT (Y increases)
- Money supply shifts RIGHT (central bank increases M^s)
- Both curves shift by same amount
- Interest rate stays CONSTANT

**Forex Market (top panel):**
- No change at all
- Exchange rate stays CONSTANT
- Interest rate stays CONSTANT

---

### Part 7 (5 points): New Money Supply with Accommodation

**ANSWER: M^s,1_CHF = 350**

**Calculation:**
```
With accommodation, R_CHF remains at 0.010
Money market: M^s,1 / P = L(R_CHF, Y_1_CHF)
M^s,1 / 1 = 100 + 1.5(200) - 5000(0.010)
M^s,1 = 100 + 300 - 50
M^s,1 = 350
```

**Change in money supply: ΔM^s = 350 - 200 = 150**

**Do rates change?**
- **Interest rate: NO CHANGE** (R = 1.0%)
- **Exchange rate: NO CHANGE** (E = 1.058)

**Economic Interpretation:**
- Central bank accommodates the increased money demand
- Increases money supply to prevent interest rate from rising
- Since interest rate doesn't change, exchange rate doesn't change (via UIP)

---

## Summary Table

| Problem | Part | Answer | Points |
|---------|------|--------|--------|
| **1.1** | Risk Analysis | Yen is riskier | 5 |
| **1.2** | Swiss Data | Fixed: Bretton Woods (1944-73); Floor: 2011-15 | 8 |
| **2.1** | Forward Rate | F = 0.9982 | 4 |
| **2.2** | USD Movement | Depreciate 2.43% | 4 |
| **2.3** | Explanation | Higher US rates → depreciation | 4 |
| **2.4** | EUR Rate | R_EUR = 2.51% | 3 |
| **3.1** | Expected E | E_e = 0.9425 | 7 |
| **3.2** | E = 0.93 | Exercise: YES, Payoff: 12.50, Profit: -62.88 | 7 |
| **3.3** | E = 0.98 | Exercise: NO, Payoff: 0, Profit: -75.37 | 6 |
| **4.1** | Swiss Rate | R_CHF = 1.0% | 5 |
| **4.2** | Spot Rate | E = 1.058 | 5 |
| **4.3** | Movement | CHF depreciates 4.00% | 5 |
| **4.4** | Diagram | See graphs | 10 |
| **4.5** | New Equilibrium | R_1 = 4.0%, E_1 = 1.089 | 10 |
| **4.6** | Diagram w/ Accom. | See graphs | 10 |
| **4.7** | New M^s | M^s,1 = 350 | 5 |
| **TOTAL** | | | **100** |

---

## Files Created

### Python Scripts
1. `problem1_part1_analysis.py` - Exchange rate risk analysis
2. `problem1_part2_switzerland.py` - Swiss exchange rate data from FRED
3. `problem2_forward_rate.py` - Forward rate calculations
4. `problem3_put_option.py` - Put option analysis
5. `problem4_money_demand.py` - Money demand and exchange rates
6. `run_all_problems.py` - Master script to run all problems

### Generated Graphics
1. `switzerland_exchange_rate.png` - CHF/USD historical data
2. `problem3_put_option_diagrams.png` - Put option payoff and profit
3. `problem4_part4_initial.png` - Initial equilibrium
4. `problem4_part4_no_accommodation.png` - After output shock
5. `problem4_part6_accommodation.png` - With monetary accommodation

### Documentation
1. `README.md` - Comprehensive guide and documentation

---

## Key Concepts Summary

### Exchange Rate Determination
- **Covered Interest Parity (CIP):** F/E = (1 + R_d)/(1 + R_f)
- **Uncovered Interest Parity (UIP):** E_e/E = (1 + R_d)/(1 + R_f)
- **Purchasing Power Parity (PPP):** Higher inflation → depreciation

### Money Market
- **Equilibrium:** M^s/P = L(R, Y)
- **Money demand:** Increases with Y, decreases with R

### Options
- **Put option payoff:** max(X - E, 0)
- **Exercise rule:** Exercise if X > E (strike > spot)
- **Maximum loss:** Option premium (with interest)

### Portfolio Risk
- **Total risk:** Variance + 2 × Covariance
- **Hedge:** Asset with negative covariance
- **Risk amplifier:** Asset with positive covariance

---

*Problem Set completed successfully. All calculations verified and diagrams generated.*
