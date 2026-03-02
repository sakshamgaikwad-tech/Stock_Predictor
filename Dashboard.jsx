import { useState } from "react";
import { predictStock } from "../services/api";
import SearchBar from "../components/SearchBar";
import MarketCard from "../components/MarketCard";
import LoadingSpinner from "../components/LoadingSpinner";

export default function Dashboard() {
  const [symbol, setSymbol] = useState("AAPL");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchPrediction = async () => {
    try {
      setLoading(true);
      const res = await predictStock(symbol);
      setData(res.data);
      setLoading(false);
    } catch (error) {
      console.error(error);
      alert("Backend error or invalid stock symbol");
      setLoading(false);
    }
  };

  return (
    <div>
      <SearchBar
        symbol={symbol}
        setSymbol={setSymbol}
        onSearch={fetchPrediction}
        loading={loading}
      />

      {loading && <LoadingSpinner />}

      {data && !loading && <MarketCard data={data} />}
    </div>
  );
}