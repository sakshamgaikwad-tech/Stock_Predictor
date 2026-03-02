import { useEffect, useRef } from "react";
import { createChart } from "lightweight-charts";

const ChartArea = () => {
  const chartRef = useRef();

  useEffect(() => {
    const chart = createChart(chartRef.current, {
      width: chartRef.current.clientWidth,
      height: 400,
      layout: {
        background: { color: "#0f172a" },
        textColor: "#d1d5db",
      },
      grid: {
        vertLines: { color: "#1e293b" },
        horzLines: { color: "#1e293b" },
      },
    });

    const candleSeries = chart.addCandlestickSeries();

    candleSeries.setData([
      { time: "2024-01-01", open: 100, high: 110, low: 90, close: 105 },
      { time: "2024-01-02", open: 105, high: 115, low: 95, close: 108 },
      { time: "2024-01-03", open: 108, high: 120, low: 100, close: 115 },
    ]);

    return () => chart.remove();
  }, []);

  return <div ref={chartRef} className="chart-container"></div>;
};

export default ChartArea;