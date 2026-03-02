import RiskBadge from "./RiskBadge";

export default function MarketCard({ data }) {
  return (
    <div className="market-card">
      <h2>Market Analysis for {data.stock_symbol}</h2>

      <p>Current Price: ₹ {data.analysis.current_price}</p>
      <p>Predicted Price: ₹ {data.analysis.predicted_price}</p>
      <p>Trend: {data.analysis.trend}</p>
      <p>Expected Profit: {data.analysis.expected_profit_percent}%</p>
      <p>Target: ₹ {data.analysis.suggested_target}</p>
      <p>Stop Loss: ₹ {data.analysis.suggested_stop_loss}</p>

      <RiskBadge level={data.analysis.risk_level} />
    </div>
  );
}