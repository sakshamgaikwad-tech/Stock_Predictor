const TradePanel = () => {
  return (
    <div className="card">
      <h3>Place Order</h3>
      <input placeholder="Price" />
      <input placeholder="Quantity" />
      <button className="buy-btn">Buy</button>
      <button className="sell-btn">Sell</button>
    </div>
  );
};

export default TradePanel;