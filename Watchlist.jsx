const Watchlist = () => {
  const stocks = ["AAPL", "TSLA", "GOOGL", "RELIANCE", "TCS"];

  return (
    <div className="card">
      <h3>Watchlist</h3>
      {stocks.map((stock) => (
        <div key={stock} className="watch-item">
          {stock}
        </div>
      ))}
    </div>
  );
};

export default Watchlist;