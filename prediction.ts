export interface PredictionResponse {
  stock_symbol: string;
  current_price: number;
  predicted_price: number;
  trend: string;
  expected_profit_percent: number;
  suggested_target: number;
  suggested_stop_loss: number;
}