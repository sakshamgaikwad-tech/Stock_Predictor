export default function SearchBar({ symbol, setSymbol, onSearch, loading }) {
  return (
    <div className="search-container">
      <input
        value={symbol}
        onChange={(e) => setSymbol(e.target.value)}
        placeholder="Enter Stock Symbol (AAPL / RELIANCE.NS)"
        className="search-input"
      />
      <button onClick={onSearch} className="search-button">
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </div>
  );
}