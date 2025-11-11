# Monetary Policy Interactive Diagram

## Overview

This interactive React component provides a comprehensive educational tool for understanding monetary policy transmission mechanisms, covering key concepts from the Global Business Environment course.

## Features

### 1. **Three Policy Scenarios**
- **Monetary Expansion**: Visualizes how increasing money supply affects interest rates, exchange rates, and the real economy
- **Monetary Contraction**: Shows the opposite effects of decreasing money supply
- **Taylor Rule**: Demonstrates how central banks systematically respond to inflation and output gaps

### 2. **Interactive Graphs**
The component includes four interactive visualizations:

#### a) Money Market Equilibrium
- **Concept**: Shows how money supply (Ms) and money demand L(R,Y) determine the equilibrium interest rate
- **Formula**: Ms/P = L(R,Y) = k₁Y - k₂R
- **Interactive Elements**:
  - Adjust money supply to see how interest rate responds
  - Modify real income to shift money demand
- **Key Insight**: When Ms ↑, the interest rate R ↓ to restore equilibrium

#### b) Interest Parity & Exchange Rate (UIP)
- **Concept**: Uncovered Interest Parity shows how interest rate differentials drive exchange rate movements
- **Formula**: R_CHF = R_EUR + (E^e - E)/E
- **Interactive Elements**:
  - Compare domestic vs. foreign interest rates
  - See how rate differentials affect currency strength
- **Key Insight**: Higher domestic rates → currency appreciates (E ↓)

#### c) Taylor Rule Policy Response
- **Concept**: Central bank's systematic monetary policy reaction function
- **Formula**: R = R* + 1.5(π - π*) + 0.5(y - y*)
- **Interactive Elements**:
  - Adjust inflation to see policy rate response
  - Modify output gap to see counter-cyclical response
- **Key Insight**: The coefficient 1.5 on inflation ensures real rates rise when inflation increases

#### d) GDP Components Impact
- **Concept**: Shows how monetary policy affects different components of GDP
- **Formula**: Y = C + I + G + NX
- **Interactive Elements**:
  - See how interest rate changes affect consumption (C) and investment (I)
  - Observe exchange rate effects on net exports (NX)
- **Key Insight**: Investment is most sensitive to interest rate changes

### 3. **Core Economic Relationships**

The component displays four fundamental identities:

1. **Money Market Equilibrium**: Ms/P = L(R, Y)
2. **Uncovered Interest Parity**: R_CHF = R_EUR + (E^e - E)/E
3. **Taylor Rule**: R = R* + f_π(π - π*) + f_y(y - y*)
4. **National Income Identity**: Y = C + I + G + CA

Also shows the savings identity: **CA = (S_p - I) + (T - G)**

### 4. **Transmission Channels**

Three main channels through which monetary policy affects the economy:

1. **Interest Rate Channel**
   - Policy Rate ↑ → All Rates ↑ → Borrowing Costs ↑ → Investment ↓ & Consumption ↓ → AD ↓

2. **Exchange Rate Channel**
   - R_domestic ↑ → Currency Appreciates → Exports ↓ & Imports ↑ → Net Exports ↓ → AD ↓

3. **Wealth/Asset Channel**
   - Interest Rates ↑ → Bond & Stock Prices ↓ → Household Wealth ↓ → Consumption ↓ → AD ↓

## Usage Instructions

### Setting Up

1. **Prerequisites**:
   ```bash
   npm install react lucide-react
   ```

2. **Import the component**:
   ```jsx
   import MonetaryPolicyDiagram from './MonetaryPolicyDiagram';
   ```

3. **Add Tailwind CSS** to your project for styling

### Interactive Scenarios

Try these scenarios to understand different economic situations:

#### Scenario 1: Fighting Inflation (Hawkish Policy)
1. Set Inflation to 4%
2. Set Output Gap to 2% (economy overheating)
3. Observe:
   - Taylor Rule prescribes R = 2% + 1.5(2%) + 0.5(2%) = 6%
   - Real rate = 6% - 4% = 2%
   - This tight policy cools the economy

#### Scenario 2: Recession Response (Dovish Policy)
1. Set Money Supply to 130
2. Set Output Gap to -3%
3. Set Inflation to 1%
4. Observe:
   - Interest rate falls
   - Currency depreciates (E ↑)
   - Net exports become more competitive
   - Taylor Rule suggests low rates to stimulate economy

#### Scenario 3: Foreign Rate Shock
1. Increase Foreign Interest Rate to 4%
2. Keep domestic settings constant
3. Observe:
   - Domestic currency appreciates
   - Net exports decline
   - This illustrates the constraint on monetary policy in open economies

#### Scenario 4: Income Growth
1. Increase Real Income (Y) to 130
2. Keep Money Supply constant at 100
3. Observe:
   - Money demand increases
   - Interest rate rises to clear the money market
   - This shows the endogenous response of interest rates to growth

## Theoretical Concepts Illustrated

### 1. Money Market Mechanics
The money market graph shows:
- **Money Demand Curve** (downward sloping): Higher interest rates reduce money demand
- **Money Supply** (vertical line): Set exogenously by the central bank
- **Equilibrium**: Where supply meets demand

### 2. Interest Parity Condition
The UIP graph illustrates:
- How arbitrage keeps returns equalized across currencies
- Why interest rate differentials drive exchange rate expectations
- The inverse relationship between domestic rates and exchange rates

### 3. Taylor Principle
The Taylor Rule graph demonstrates:
- **f_π > 1**: Crucial for stability - nominal rate must rise more than inflation
- **Counter-cyclical policy**: Positive output gap → tighten; negative gap → loosen
- The systematic, predictable nature of modern monetary policy

### 4. National Accounting Identities
The component emphasizes:
- **Twin Deficits**: Government deficit (T-G < 0) often correlates with current account deficit (CA < 0)
- **Savings Identity**: CA = (S_p - I) + (T - G)
- How private savings collapse (observed in US data after 1990) affects the current account

## Educational Applications

### For Students:
- **Before Class**: Explore basic scenarios to build intuition
- **During Class**: Use alongside lectures to visualize theoretical concepts
- **After Class**: Test understanding by predicting effects before adjusting sliders

### For Instructors:
- **Lectures**: Project the interactive graphs during explanations
- **Problem Sets**: Reference specific parameter combinations
- **Exams**: Ask students to predict outcomes for given policy changes

## Real-World Applications

### Central Bank Policy
The component helps understand:
- Why central banks raise rates aggressively when inflation rises
- How exchange rate movements amplify or dampen monetary policy
- The trade-offs between inflation control and output stabilization

### Historical Episodes
Can be used to analyze:
- **2008 Financial Crisis**: Low rates, near-zero lower bound
- **2020 COVID Response**: Massive monetary expansion
- **2022-2023 Inflation**: Aggressive rate hiking cycle
- **1990s US Economy**: Twin deficits and private savings collapse (from Problem Set 1)

## Technical Details

### Key Parameters
- **k₁ = 0.5**: Income elasticity of money demand
- **k₂ = 20**: Interest rate semi-elasticity of money demand
- **R* = 2%**: Equilibrium/neutral interest rate
- **f_π = 1.5**: Taylor Rule inflation coefficient (must be > 1)
- **f_y = 0.5**: Taylor Rule output gap coefficient
- **π* = 2%**: Inflation target

### Calculation Methods
```javascript
// Interest Rate from Money Market
R = (k₁ × Y - Ms) / k₂

// Exchange Rate from UIP (simplified)
E = base × exp(-0.1 × (R_domestic - R_foreign))

// Taylor Rule
R = R* + f_π × (π - π*) + f_y × (y - y*)

// GDP Impact
C = baseline + rate_effect × 0.3
I = baseline + rate_effect × 1.0  // Most sensitive
NX = baseline + exchange_rate_effect
```

## Connection to Course Material

### From Problem Set 1 (Twin Deficits)
The component incorporates findings from the US data analysis (1960-2024):
- National accounting identity: **CA = (S_p - I) + (T - G)**
- Correlation between government and current account deficits
- The role of private savings in determining the current account
- How the relationship changed after 1990 due to private savings collapse

### Key Empirical Insights:
- Before 1990: Strong correlation (r = 0.82) between budget and CA deficits
- After 1990: Weaker correlation (r = 0.53) but larger structural deficits
- Private savings declined from 8.05% to 4.67% of GDP
- This made the US more dependent on foreign capital

## Pedagogical Benefits

1. **Visual Learning**: Graphs update in real-time as parameters change
2. **Causal Understanding**: Clear transmission channels show how policy affects outcomes
3. **Quantitative Intuition**: Numerical values help students calibrate magnitudes
4. **Multiple Representations**: Same concepts shown through flows, graphs, and formulas
5. **Active Learning**: Students engage by testing predictions

## Limitations & Simplifications

1. **Static Analysis**: No dynamics or lags in the model
2. **Simplified UIP**: Assumes static exchange rate expectations
3. **Linear Relationships**: Real economy has non-linearities
4. **Closed Form Solutions**: Actual models are more complex
5. **Omitted Channels**: Credit channel, expectations channel not explicitly modeled

## Extensions & Future Work

Potential enhancements:
- Add IS-LM-BP model for simultaneous equilibrium
- Include Phillips Curve for inflation dynamics
- Add expectations formation mechanisms
- Show impulse response functions over time
- Include financial frictions and credit markets

## References

Based on course material covering:
- Money market equilibrium
- Uncovered Interest Parity (UIP)
- Taylor Rule monetary policy
- National income accounting
- Monetary policy transmission mechanisms
- Twin deficits hypothesis
- Open economy macroeconomics

## Conclusion

This interactive tool bridges theory and practice, allowing students to:
- **Visualize** abstract economic concepts
- **Experiment** with policy scenarios
- **Understand** transmission mechanisms
- **Connect** micro foundations to macro outcomes
- **Apply** theoretical knowledge to real-world situations

The component serves as a comprehensive educational resource for monetary economics, suitable for undergraduate and graduate courses in macroeconomics, international finance, and monetary policy.
