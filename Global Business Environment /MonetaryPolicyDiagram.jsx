import React, { useState } from 'react';
import { ArrowRight, TrendingUp, TrendingDown, LineChart } from 'lucide-react';

const MonetaryPolicyDiagram = () => {
  const [activeScenario, setActiveScenario] = useState('expansion');
  const [showGraphs, setShowGraphs] = useState(false);
  
  // Graph parameters
  const [moneySupply, setMoneySupply] = useState(100);
  const [income, setIncome] = useState(100);
  const [foreignRate, setForeignRate] = useState(2);
  const [inflation, setInflation] = useState(2);
  const [outputGap, setOutputGap] = useState(0);

  // Calculate equilibrium interest rate from money market
  const calcInterestRate = (ms, y) => {
    // L(R,Y) = k1*Y - k2*R, where k1=0.5, k2=20
    // Money market equilibrium: Ms/P = L(R,Y)
    // Assuming P=1 for simplicity: Ms = k1*Y - k2*R
    // R = (k1*Y - Ms)/k2
    const k1 = 0.5;
    const k2 = 20;
    const rate = Math.max(0, (k1 * y - ms) / k2);
    return rate;
  };

  // Calculate exchange rate from UIP
  const calcExchangeRate = (domesticRate, foreignRate) => {
    // Simplified: E = base * (1 + rate_differential)
    // Higher domestic rate → currency appreciates → E falls
    const base = 1.0;
    const rateDiff = domesticRate - foreignRate;
    return base * Math.exp(-rateDiff * 0.1); // E decreases when R_dom > R_for
  };

  // Calculate Taylor Rule rate
  const calcTaylorRate = (inflationRate, inflationTarget, outputGap) => {
    const rStar = 2; // equilibrium rate
    const fPi = 1.5;
    const fY = 0.5;
    return rStar + fPi * (inflationRate - inflationTarget) + fY * outputGap;
  };

  const domesticRate = calcInterestRate(moneySupply, income);
  const exchangeRate = calcExchangeRate(domesticRate, foreignRate);
  const taylorRate = calcTaylorRate(inflation, 2, outputGap);

  // Generate points for money demand curve
  const generateMoneyDemandCurve = (y) => {
    const points = [];
    for (let r = 0; r <= 8; r += 0.2) {
      const md = 0.5 * y - 20 * r; // L(R,Y) = k1*Y - k2*R
      if (md > 0) {
        points.push({ r, md });
      }
    }
    return points;
  };

  // Generate points for UIP curve
  const generateUIPCurve = (rFor) => {
    const points = [];
    for (let rDom = 0; rDom <= 8; rDom += 0.2) {
      const e = calcExchangeRate(rDom, rFor);
      points.push({ rDom, e });
    }
    return points;
  };

  const moneyDemandPoints = generateMoneyDemandCurve(income);
  const uipPoints = generateUIPCurve(foreignRate);

  const scenarios = {
    expansion: {
      title: 'Monetary Expansion (Ms ↑)',
      color: 'blue',
      steps: [
        { label: 'Central Bank', action: 'Increases Money Supply (Ms ↑)', color: 'bg-blue-100' },
        { label: 'Money Market', action: 'Interest Rate Falls (R ↓)', color: 'bg-blue-200' },
        { label: 'FX Market', action: 'Currency Depreciates (E ↑)', color: 'bg-blue-300' },
        { label: 'Real Economy', action: 'Investment ↑, Exports ↑, AD ↑', color: 'bg-blue-400' }
      ]
    },
    contraction: {
      title: 'Monetary Contraction (Ms ↓)',
      color: 'red',
      steps: [
        { label: 'Central Bank', action: 'Decreases Money Supply (Ms ↓)', color: 'bg-red-100' },
        { label: 'Money Market', action: 'Interest Rate Rises (R ↑)', color: 'bg-red-200' },
        { label: 'FX Market', action: 'Currency Appreciates (E ↓)', color: 'bg-red-300' },
        { label: 'Real Economy', action: 'Investment ↓, Exports ↓, AD ↓', color: 'bg-red-400' }
      ]
    },
    taylor: {
      title: 'Taylor Rule Response to High Inflation',
      color: 'orange',
      steps: [
        { label: 'Shock', action: 'Inflation Above Target (π > π*)', color: 'bg-orange-100' },
        { label: 'Taylor Rule', action: 'R = R* + 1.5(π - π*) + 0.5(y - y*)', color: 'bg-orange-200' },
        { label: 'Policy Action', action: 'Raise R aggressively (by > 1% per 1% inflation)', color: 'bg-orange-300' },
        { label: 'Effect', action: 'Real Rate ↑ → Borrowing ↓ → AD ↓ → π ↓', color: 'bg-orange-400' }
      ]
    }
  };

  return (
    <div className="w-full max-w-6xl mx-auto p-6 bg-gray-50">
      <h1 className="text-3xl font-bold text-center mb-8 text-gray-800">
        Monetary Policy Transmission Mechanism
      </h1>

      {/* Scenario Selector */}
      <div className="flex gap-4 mb-8 justify-center flex-wrap">
        <button
          onClick={() => setActiveScenario('expansion')}
          className={`px-6 py-3 rounded-lg font-semibold transition-all ${
            activeScenario === 'expansion'
              ? 'bg-blue-500 text-white shadow-lg'
              : 'bg-white text-gray-700 hover:bg-gray-100'
          }`}
        >
          Monetary Expansion
        </button>
        <button
          onClick={() => setActiveScenario('contraction')}
          className={`px-6 py-3 rounded-lg font-semibold transition-all ${
            activeScenario === 'contraction'
              ? 'bg-red-500 text-white shadow-lg'
              : 'bg-white text-gray-700 hover:bg-gray-100'
          }`}
        >
          Monetary Contraction
        </button>
        <button
          onClick={() => setActiveScenario('taylor')}
          className={`px-6 py-3 rounded-lg font-semibold transition-all ${
            activeScenario === 'taylor'
              ? 'bg-orange-500 text-white shadow-lg'
              : 'bg-white text-gray-700 hover:bg-gray-100'
          }`}
        >
          Taylor Rule
        </button>
        <button
          onClick={() => setShowGraphs(!showGraphs)}
          className={`px-6 py-3 rounded-lg font-semibold transition-all flex items-center gap-2 ${
            showGraphs
              ? 'bg-green-500 text-white shadow-lg'
              : 'bg-white text-gray-700 hover:bg-gray-100'
          }`}
        >
          <LineChart size={20} />
          {showGraphs ? 'Hide Graphs' : 'Show Interactive Graphs'}
        </button>
      </div>

      {/* Interactive Graphs Section */}
      {showGraphs && (
        <div className="bg-white rounded-xl shadow-lg p-8 mb-8">
          <h2 className="text-2xl font-bold mb-6 text-center text-gray-800">
            Interactive Graph Plotter
          </h2>

          {/* Controls */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
            {/* Money Supply Slider */}
            <div className="bg-blue-50 p-4 rounded-lg border-2 border-blue-200">
              <label className="block text-sm font-bold mb-2 text-blue-800">
                Money Supply (Ms): {moneySupply}
              </label>
              <input
                type="range"
                min="50"
                max="150"
                value={moneySupply}
                onChange={(e) => setMoneySupply(Number(e.target.value))}
                className="w-full"
              />
              <div className="text-xs text-gray-600 mt-1">
                Increase → R↓, E↑ (depreciation)
              </div>
            </div>

            {/* Income Slider */}
            <div className="bg-green-50 p-4 rounded-lg border-2 border-green-200">
              <label className="block text-sm font-bold mb-2 text-green-800">
                Real Income (Y): {income}
              </label>
              <input
                type="range"
                min="50"
                max="150"
                value={income}
                onChange={(e) => setIncome(Number(e.target.value))}
                className="w-full"
              />
              <div className="text-xs text-gray-600 mt-1">
                Increase → Money demand↑ → R↑
              </div>
            </div>

            {/* Foreign Rate Slider */}
            <div className="bg-purple-50 p-4 rounded-lg border-2 border-purple-200">
              <label className="block text-sm font-bold mb-2 text-purple-800">
                Foreign Interest Rate: {foreignRate.toFixed(1)}%
              </label>
              <input
                type="range"
                min="0"
                max="6"
                step="0.1"
                value={foreignRate}
                onChange={(e) => setForeignRate(Number(e.target.value))}
                className="w-full"
              />
              <div className="text-xs text-gray-600 mt-1">
                Increase → Domestic currency appreciates
              </div>
            </div>

            {/* Inflation Slider */}
            <div className="bg-orange-50 p-4 rounded-lg border-2 border-orange-200">
              <label className="block text-sm font-bold mb-2 text-orange-800">
                Inflation (π): {inflation.toFixed(1)}%
              </label>
              <input
                type="range"
                min="0"
                max="6"
                step="0.1"
                value={inflation}
                onChange={(e) => setInflation(Number(e.target.value))}
                className="w-full"
              />
              <div className="text-xs text-gray-600 mt-1">
                Target: 2% | Current deviation: {(inflation - 2).toFixed(1)}%
              </div>
            </div>

            {/* Output Gap Slider */}
            <div className="bg-teal-50 p-4 rounded-lg border-2 border-teal-200">
              <label className="block text-sm font-bold mb-2 text-teal-800">
                Output Gap (y-y*): {outputGap.toFixed(1)}%
              </label>
              <input
                type="range"
                min="-5"
                max="5"
                step="0.1"
                value={outputGap}
                onChange={(e) => setOutputGap(Number(e.target.value))}
                className="w-full"
              />
              <div className="text-xs text-gray-600 mt-1">
                Positive = overheating | Negative = recession
              </div>
            </div>

            {/* Results Display */}
            <div className="bg-gray-50 p-4 rounded-lg border-2 border-gray-300">
              <div className="text-sm font-bold mb-2 text-gray-800">Current Values:</div>
              <div className="space-y-1 text-sm">
                <div>Interest Rate: <span className="font-bold text-blue-600">{domesticRate.toFixed(2)}%</span></div>
                <div>Exchange Rate: <span className="font-bold text-green-600">{exchangeRate.toFixed(3)}</span></div>
                <div>Taylor Rate: <span className="font-bold text-orange-600">{taylorRate.toFixed(2)}%</span></div>
                <div className="text-xs text-gray-500 mt-2">
                  Real Rate: {(domesticRate - inflation).toFixed(2)}%
                </div>
              </div>
            </div>
          </div>

          {/* Graphs */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {/* Money Market Graph */}
            <div className="border-2 border-blue-300 rounded-lg p-6 bg-blue-50">
              <h3 className="text-lg font-bold mb-4 text-blue-800 text-center">
                Money Market Equilibrium
              </h3>
              <div className="bg-white p-4 rounded relative" style={{ height: '300px' }}>
                <svg width="100%" height="100%" viewBox="0 0 400 300">
                  {/* Axes */}
                  <line x1="50" y1="250" x2="350" y2="250" stroke="black" strokeWidth="2" />
                  <line x1="50" y1="250" x2="50" y2="30" stroke="black" strokeWidth="2" />
                  
                  {/* Labels */}
                  <text x="200" y="280" textAnchor="middle" fontSize="12">Real Money (M/P)</text>
                  <text x="20" y="140" textAnchor="middle" fontSize="12" transform="rotate(-90 20 140)">Interest Rate (R)</text>
                  
                  {/* Money Demand Curve */}
                  <path
                    d={`M ${moneyDemandPoints.map((p, i) => 
                      `${i === 0 ? 'M' : 'L'} ${50 + p.md * 2.5} ${250 - p.r * 25}`
                    ).join(' ')}`}
                    stroke="blue"
                    strokeWidth="3"
                    fill="none"
                  />
                  
                  {/* Money Supply Line (vertical) */}
                  <line 
                    x1={50 + moneySupply * 2.5} 
                    y1="250" 
                    x2={50 + moneySupply * 2.5} 
                    y2="30" 
                    stroke="red" 
                    strokeWidth="3" 
                    strokeDasharray="5,5"
                  />
                  
                  {/* Equilibrium Point */}
                  <circle 
                    cx={50 + moneySupply * 2.5} 
                    cy={250 - domesticRate * 25} 
                    r="6" 
                    fill="green" 
                    stroke="darkgreen" 
                    strokeWidth="2"
                  />
                  
                  {/* Legend */}
                  <line x1="270" y1="50" x2="300" y2="50" stroke="blue" strokeWidth="3" />
                  <text x="305" y="55" fontSize="11">L(R,Y) - Demand</text>
                  
                  <line x1="270" y1="70" x2="300" y2="70" stroke="red" strokeWidth="3" strokeDasharray="5,5" />
                  <text x="305" y="75" fontSize="11">Ms/P - Supply</text>
                  
                  <circle cx="285" cy="90" r="4" fill="green" />
                  <text x="295" y="95" fontSize="11">Equilibrium</text>
                </svg>
              </div>
              <div className="mt-3 text-sm text-gray-700 bg-white p-3 rounded">
                <strong>Equilibrium:</strong> R = {domesticRate.toFixed(2)}% where money supply meets money demand
              </div>
            </div>

            {/* Exchange Rate Graph */}
            <div className="border-2 border-green-300 rounded-lg p-6 bg-green-50">
              <h3 className="text-lg font-bold mb-4 text-green-800 text-center">
                Interest Parity & Exchange Rate
              </h3>
              <div className="bg-white p-4 rounded relative" style={{ height: '300px' }}>
                <svg width="100%" height="100%" viewBox="0 0 400 300">
                  {/* Axes */}
                  <line x1="50" y1="250" x2="350" y2="250" stroke="black" strokeWidth="2" />
                  <line x1="50" y1="250" x2="50" y2="30" stroke="black" strokeWidth="2" />
                  
                  {/* Labels */}
                  <text x="200" y="280" textAnchor="middle" fontSize="12">Domestic Interest Rate</text>
                  <text x="20" y="140" textAnchor="middle" fontSize="12" transform="rotate(-90 20 140)">Exchange Rate (E)</text>
                  
                  {/* UIP Curve */}
                  <path
                    d={`M ${uipPoints.map((p, i) => 
                      `${i === 0 ? 'M' : 'L'} ${50 + p.rDom * 35} ${250 - p.e * 150}`
                    ).join(' ')}`}
                    stroke="purple"
                    strokeWidth="3"
                    fill="none"
                  />
                  
                  {/* Current Point */}
                  <circle 
                    cx={50 + domesticRate * 35} 
                    cy={250 - exchangeRate * 150} 
                    r="6" 
                    fill="red" 
                    stroke="darkred" 
                    strokeWidth="2"
                  />
                  
                  {/* Foreign Rate Reference Line */}
                  <line 
                    x1={50 + foreignRate * 35} 
                    y1="250" 
                    x2={50 + foreignRate * 35} 
                    y2="30" 
                    stroke="orange" 
                    strokeWidth="2" 
                    strokeDasharray="3,3"
                    opacity="0.5"
                  />
                  
                  {/* Legend */}
                  <line x1="250" y1="50" x2="280" y2="50" stroke="purple" strokeWidth="3" />
                  <text x="285" y="55" fontSize="11">UIP Condition</text>
                  
                  <circle cx="265" cy="70" r="4" fill="red" />
                  <text x="275" y="75" fontSize="11">Current (R, E)</text>
                  
                  <line x1="250" y1="85" x2="280" y2="85" stroke="orange" strokeWidth="2" strokeDasharray="3,3" />
                  <text x="285" y="90" fontSize="11">Foreign R</text>
                </svg>
              </div>
              <div className="mt-3 text-sm text-gray-700 bg-white p-3 rounded">
                <strong>UIP:</strong> R<sub>CHF</sub> ({domesticRate.toFixed(2)}%) vs R<sub>EUR</sub> ({foreignRate.toFixed(1)}%) 
                → E = {exchangeRate.toFixed(3)} {domesticRate > foreignRate ? '(CHF strong)' : '(CHF weak)'}
              </div>
            </div>

            {/* Taylor Rule Graph */}
            <div className="border-2 border-orange-300 rounded-lg p-6 bg-orange-50">
              <h3 className="text-lg font-bold mb-4 text-orange-800 text-center">
                Taylor Rule Policy Response
              </h3>
              <div className="bg-white p-4 rounded relative" style={{ height: '300px' }}>
                <svg width="100%" height="100%" viewBox="0 0 400 300">
                  {/* Axes */}
                  <line x1="50" y1="150" x2="350" y2="150" stroke="black" strokeWidth="2" />
                  <line x1="200" y1="250" x2="200" y2="30" stroke="black" strokeWidth="2" />
                  
                  {/* Grid lines */}
                  <line x1="50" y1="100" x2="350" y2="100" stroke="gray" strokeWidth="1" opacity="0.2" />
                  <line x1="50" y1="200" x2="350" y2="200" stroke="gray" strokeWidth="1" opacity="0.2" />
                  
                  {/* Labels */}
                  <text x="200" y="280" textAnchor="middle" fontSize="12">Inflation - Target (%)</text>
                  <text x="20" y="140" textAnchor="middle" fontSize="12" transform="rotate(-90 20 140)">Policy Rate (%)</text>
                  
                  {/* Taylor Rule Line for current output gap */}
                  {[-3, -2, -1, 0, 1, 2, 3].map((inflDev, idx, arr) => {
                    if (idx === arr.length - 1) return null;
                    const nextInflDev = arr[idx + 1];
                    const r1 = 2 + 1.5 * inflDev + 0.5 * outputGap;
                    const r2 = 2 + 1.5 * nextInflDev + 0.5 * outputGap;
                    return (
                      <line
                        key={idx}
                        x1={200 + inflDev * 40}
                        y1={150 - r1 * 15}
                        x2={200 + nextInflDev * 40}
                        y2={150 - r2 * 15}
                        stroke="orange"
                        strokeWidth="3"
                      />
                    );
                  })}
                  
                  {/* Current Position */}
                  <circle 
                    cx={200 + (inflation - 2) * 40} 
                    cy={150 - taylorRate * 15} 
                    r="6" 
                    fill="red" 
                    stroke="darkred" 
                    strokeWidth="2"
                  />
                  
                  {/* Target inflation line */}
                  <line 
                    x1="200" 
                    y1="30" 
                    x2="200" 
                    y2="250" 
                    stroke="green" 
                    strokeWidth="2" 
                    strokeDasharray="5,5"
                    opacity="0.5"
                  />
                  
                  {/* Legend */}
                  <text x="260" y="50" fontSize="11" fill="green">π = π* (target)</text>
                  <circle cx="280" cy="70" r="4" fill="red" />
                  <text x="290" y="75" fontSize="11">Current policy</text>
                </svg>
              </div>
              <div className="mt-3 text-sm text-gray-700 bg-white p-3 rounded">
                <strong>Taylor Rule:</strong> R = 2% + 1.5×({(inflation-2).toFixed(1)}%) + 0.5×({outputGap.toFixed(1)}%) = {taylorRate.toFixed(2)}%
                <br/><span className="text-xs">Real rate = {(taylorRate - inflation).toFixed(2)}%</span>
              </div>
            </div>

            {/* GDP Components Impact */}
            <div className="border-2 border-indigo-300 rounded-lg p-6 bg-indigo-50">
              <h3 className="text-lg font-bold mb-4 text-indigo-800 text-center">
                Policy Impact on GDP Components
              </h3>
              <div className="bg-white p-4 rounded" style={{ height: '300px' }}>
                <svg width="100%" height="100%" viewBox="0 0 400 300">
                  {/* Calculate impacts based on current settings */}
                  {(() => {
                    const baseline = 100;
                    const rateEffect = (domesticRate - 2) * -5; // Higher R reduces spending
                    const exRateEffect = (1 - exchangeRate) * 100; // Appreciation reduces NX
                    
                    const consumption = Math.max(0, baseline + rateEffect * 0.3);
                    const investment = Math.max(0, baseline + rateEffect * 1.0);
                    const government = baseline; // Assumed constant
                    const netExports = Math.max(-50, baseline + exRateEffect);
                    
                    const bars = [
                      { label: 'C', value: consumption, color: '#3b82f6', x: 70 },
                      { label: 'I', value: investment, color: '#8b5cf6', x: 150 },
                      { label: 'G', value: government, color: '#10b981', x: 230 },
                      { label: 'NX', value: netExports, color: '#f59e0b', x: 310 }
                    ];
                    
                    return (
                      <>
                        {/* Baseline line */}
                        <line x1="40" y1="150" x2="360" y2="150" stroke="gray" strokeWidth="1" strokeDasharray="3,3" />
                        <text x="365" y="155" fontSize="10" fill="gray">Baseline</text>
                        
                        {/* Bars */}
                        {bars.map((bar, idx) => {
                          const height = Math.abs(bar.value - baseline) * 1.5;
                          const y = bar.value >= baseline ? 150 - height : 150;
                          return (
                            <g key={idx}>
                              <rect
                                x={bar.x - 25}
                                y={y}
                                width="50"
                                height={height}
                                fill={bar.color}
                                opacity="0.8"
                              />
                              <text
                                x={bar.x}
                                y="270"
                                textAnchor="middle"
                                fontSize="14"
                                fontWeight="bold"
                              >
                                {bar.label}
                              </text>
                              <text
                                x={bar.x}
                                y={y - 5}
                                textAnchor="middle"
                                fontSize="11"
                                fill={bar.color}
                              >
                                {bar.value.toFixed(0)}
                              </text>
                            </g>
                          );
                        })}
                        
                        {/* Axis */}
                        <line x1="40" y1="250" x2="360" y2="250" stroke="black" strokeWidth="2" />
                        <text x="200" y="295" textAnchor="middle" fontSize="12">GDP = C + I + G + NX</text>
                      </>
                    );
                  })()}
                </svg>
              </div>
              <div className="mt-3 text-sm text-gray-700 bg-white p-3 rounded space-y-1">
                <div><strong>Interest Rate Effect:</strong> R↑ reduces C and I (especially I)</div>
                <div><strong>Exchange Rate Effect:</strong> Strong currency reduces NX</div>
                <div className="text-xs text-gray-500 mt-2">
                  Higher R = {domesticRate.toFixed(2)}% → Tighter policy → Lower GDP
                </div>
              </div>
            </div>
          </div>

          {/* Interactive Tips */}
          <div className="mt-6 bg-gradient-to-r from-blue-50 to-green-50 rounded-lg p-6">
            <h3 className="text-lg font-bold mb-3 text-gray-800">💡 Try These Scenarios:</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
              <div className="bg-white p-3 rounded shadow-sm">
                <strong className="text-blue-600">📈 Monetary Expansion:</strong> Increase money supply to 130 → Watch R fall and E rise (depreciation)
              </div>
              <div className="bg-white p-3 rounded shadow-sm">
                <strong className="text-red-600">📉 Fight Inflation:</strong> Set inflation to 4% → See Taylor rule prescribe higher R to cool economy
              </div>
              <div className="bg-white p-3 rounded shadow-sm">
                <strong className="text-green-600">🌍 Foreign Rate Shock:</strong> Raise foreign rate to 4% → Domestic currency strengthens
              </div>
              <div className="bg-white p-3 rounded shadow-sm">
                <strong className="text-orange-600">📊 Recession Response:</strong> Set output gap to -3% → Taylor rule suggests lower rates
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Active Scenario Flow */}
      <div className="bg-white rounded-xl shadow-lg p-8 mb-8">
        <h2 className="text-2xl font-bold mb-6 text-center text-gray-800">
          {scenarios[activeScenario].title}
        </h2>
        <div className="flex items-center justify-between">
          {scenarios[activeScenario].steps.map((step, idx) => (
            <React.Fragment key={idx}>
              <div className="flex-1">
                <div className={`${step.color} rounded-lg p-6 h-32 flex flex-col justify-center items-center text-center shadow-md`}>
                  <div className="font-bold text-lg mb-2">{step.label}</div>
                  <div className="text-sm">{step.action}</div>
                </div>
              </div>
              {idx < scenarios[activeScenario].steps.length - 1 && (
                <ArrowRight className="mx-4 text-gray-400" size={32} />
              )}
            </React.Fragment>
          ))}
        </div>
      </div>

      {/* Main Relationships Diagram */}
      <div className="bg-white rounded-xl shadow-lg p-8 mb-8">
        <h2 className="text-2xl font-bold mb-6 text-center text-gray-800">
          Core Relationships & Formulas
        </h2>
        
        <div className="grid grid-cols-2 gap-6">
          {/* Money Market Equilibrium */}
          <div className="border-2 border-purple-300 rounded-lg p-6 bg-purple-50">
            <h3 className="text-xl font-bold mb-4 text-purple-800">Money Market Equilibrium</h3>
            <div className="space-y-3">
              <div className="bg-white p-3 rounded border border-purple-200">
                <div className="font-mono text-center text-lg">M<sup>s</sup>/P = L(R, Y)</div>
              </div>
              <div className="text-sm space-y-2">
                <div><strong>M<sup>s</sup></strong>: Money Supply (set by CB)</div>
                <div><strong>P</strong>: Price Level (sticky short-run)</div>
                <div><strong>R</strong>: Interest Rate (adjusts to clear market)</div>
                <div><strong>Y</strong>: Real Income</div>
              </div>
              <div className="mt-4 p-3 bg-purple-100 rounded text-sm">
                <strong>Key:</strong> R ↑ → L(R,Y) ↓ (inverse relationship)<br/>
                Y ↑ → L(R,Y) ↑ (positive relationship)
              </div>
            </div>
          </div>

          {/* Uncovered Interest Parity */}
          <div className="border-2 border-green-300 rounded-lg p-6 bg-green-50">
            <h3 className="text-xl font-bold mb-4 text-green-800">Uncovered Interest Parity (UIP)</h3>
            <div className="space-y-3">
              <div className="bg-white p-3 rounded border border-green-200">
                <div className="font-mono text-center text-lg">R<sub>CHF</sub> = R<sub>EUR</sub> + (E<sup>e</sup> - E)/E</div>
              </div>
              <div className="text-sm space-y-2">
                <div><strong>R<sub>CHF</sub></strong>: Domestic interest rate</div>
                <div><strong>R<sub>EUR</sub></strong>: Foreign interest rate</div>
                <div><strong>E</strong>: Current exchange rate (CHF/EUR)</div>
                <div><strong>E<sup>e</sup></strong>: Expected future exchange rate</div>
              </div>
              <div className="mt-4 p-3 bg-green-100 rounded text-sm">
                <strong>Key:</strong> If R<sub>CHF</sub> ↑ → CHF appreciates (E ↓)<br/>
                Returns must equalize across currencies
              </div>
            </div>
          </div>

          {/* Taylor Rule */}
          <div className="border-2 border-orange-300 rounded-lg p-6 bg-orange-50">
            <h3 className="text-xl font-bold mb-4 text-orange-800">Taylor Rule</h3>
            <div className="space-y-3">
              <div className="bg-white p-3 rounded border border-orange-200">
                <div className="font-mono text-center text-lg">R = R* + f<sub>π</sub>(π - π*) + f<sub>y</sub>(y - y*)</div>
              </div>
              <div className="text-sm space-y-2">
                <div><strong>R*</strong>: Equilibrium rate</div>
                <div><strong>π</strong>: Current inflation, <strong>π*</strong>: Target (2%)</div>
                <div><strong>y</strong>: Output, <strong>y*</strong>: Potential output</div>
                <div><strong>f<sub>π</sub></strong> = 1.5 (inflation response)</div>
                <div><strong>f<sub>y</sub></strong> = 0.5 (output response)</div>
              </div>
              <div className="mt-4 p-3 bg-orange-100 rounded text-sm">
                <strong>Key:</strong> f<sub>π</sub> {'>'}  1 ensures real rate rises<br/>
                when inflation ↑ to cool economy
              </div>
            </div>
          </div>

          {/* National Income Identity */}
          <div className="border-2 border-blue-300 rounded-lg p-6 bg-blue-50">
            <h3 className="text-xl font-bold mb-4 text-blue-800">National Income Identity</h3>
            <div className="space-y-3">
              <div className="bg-white p-3 rounded border border-blue-200">
                <div className="font-mono text-center text-lg">Y = C + I + G + CA</div>
              </div>
              <div className="text-sm space-y-2">
                <div><strong>Y</strong>: GDP/National Income</div>
                <div><strong>C</strong>: Consumption (~51%)</div>
                <div><strong>I</strong>: Investment (~27%, most volatile)</div>
                <div><strong>G</strong>: Government purchases (~12%)</div>
                <div><strong>CA</strong>: Current Account (~10%)</div>
              </div>
              <div className="mt-4 p-3 bg-blue-100 rounded text-sm">
                <strong>Saving Identity:</strong> S = I + CA<br/>
                Save domestically (I) or abroad (CA)
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Transmission Channels */}
      <div className="bg-white rounded-xl shadow-lg p-8">
        <h2 className="text-2xl font-bold mb-6 text-center text-gray-800">
          Monetary Policy Transmission Channels
        </h2>
        
        <div className="grid grid-cols-3 gap-6">
          {/* Interest Rate Channel */}
          <div className="border-2 border-indigo-300 rounded-lg p-6 bg-indigo-50">
            <h3 className="text-lg font-bold mb-4 text-indigo-800 text-center">Interest Rate Channel</h3>
            <div className="space-y-3 text-sm">
              <div className="flex items-center justify-between">
                <span>Policy Rate ↑</span>
                <ArrowRight size={16} />
              </div>
              <div className="flex items-center justify-between">
                <span>All Rates ↑</span>
                <ArrowRight size={16} />
              </div>
              <div className="flex items-center justify-between">
                <span>Borrowing Costs ↑</span>
                <ArrowRight size={16} />
              </div>
              <div className="flex items-center justify-between">
                <span>Investment ↓</span>
                <ArrowRight size={16} />
              </div>
              <div className="flex items-center justify-between">
                <span>Consumption ↓</span>
                <ArrowRight size={16} />
              </div>
              <div className="bg-indigo-100 p-2 rounded text-center font-semibold">
                Aggregate Demand ↓
              </div>
            </div>
          </div>

          {/* Exchange Rate Channel */}
          <div className="border-2 border-teal-300 rounded-lg p-6 bg-teal-50">
            <h3 className="text-lg font-bold mb-4 text-teal-800 text-center">Exchange Rate Channel</h3>
            <div className="space-y-3 text-sm">
              <div className="flex items-center justify-between">
                <span>R<sub>domestic</sub> ↑</span>
                <ArrowRight size={16} />
              </div>
              <div className="flex items-center justify-between">
                <span>Currency Appreciates</span>
                <ArrowRight size={16} />
              </div>
              <div className="flex items-center justify-between">
                <span>Exports ↓</span>
                <ArrowRight size={16} />
              </div>
              <div className="flex items-center justify-between">
                <span>Imports ↑</span>
                <ArrowRight size={16} />
              </div>
              <div className="flex items-center justify-between">
                <span>Net Exports ↓</span>
                <ArrowRight size={16} />
              </div>
              <div className="bg-teal-100 p-2 rounded text-center font-semibold">
                Aggregate Demand ↓
              </div>
            </div>
          </div>

          {/* Wealth/Asset Channel */}
          <div className="border-2 border-pink-300 rounded-lg p-6 bg-pink-50">
            <h3 className="text-lg font-bold mb-4 text-pink-800 text-center">Wealth/Asset Channel</h3>
            <div className="space-y-3 text-sm">
              <div className="flex items-center justify-between">
                <span>Interest Rates ↑</span>
                <ArrowRight size={16} />
              </div>
              <div className="flex items-center justify-between">
                <span>Bond Prices ↓</span>
                <ArrowRight size={16} />
              </div>
              <div className="flex items-center justify-between">
                <span>Stock Prices ↓</span>
                <ArrowRight size={16} />
              </div>
              <div className="flex items-center justify-between">
                <span>Household Wealth ↓</span>
                <ArrowRight size={16} />
              </div>
              <div className="flex items-center justify-between">
                <span>Consumption ↓</span>
                <ArrowRight size={16} />
              </div>
              <div className="bg-pink-100 p-2 rounded text-center font-semibold">
                Aggregate Demand ↓
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Key Takeaways */}
      <div className="mt-8 bg-gradient-to-r from-purple-100 to-blue-100 rounded-xl p-6">
        <h3 className="text-xl font-bold mb-4 text-gray-800">Key Takeaways</h3>
        <ul className="space-y-2 text-sm">
          <li className="flex items-start">
            <span className="text-purple-600 mr-2">•</span>
            <span><strong>Money Market:</strong> Central bank controls Ms, which determines R through equilibrium condition</span>
          </li>
          <li className="flex items-start">
            <span className="text-purple-600 mr-2">•</span>
            <span><strong>Exchange Rates:</strong> Interest rate differentials drive currency movements (UIP)</span>
          </li>
          <li className="flex items-start">
            <span className="text-purple-600 mr-2">•</span>
            <span><strong>Taylor Rule:</strong> Systematic policy response to inflation and output gaps (f<sub>π</sub> {'>'} 1 is crucial)</span>
          </li>
          <li className="flex items-start">
            <span className="text-purple-600 mr-2">•</span>
            <span><strong>Transmission:</strong> Monetary policy affects economy through multiple channels simultaneously</span>
          </li>
          <li className="flex items-start">
            <span className="text-purple-600 mr-2">•</span>
            <span><strong>Real Effects:</strong> Changes in R and E both impact aggregate demand (C, I, CA components)</span>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default MonetaryPolicyDiagram;
