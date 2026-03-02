from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from predict_lstm import predict_next_price
import yfinance as yf
import numpy as np

# ==============================
# 🚀 FASTAPI INITIALIZATION
# ==============================

app = FastAPI(
    title="AI Stock Market Prediction API",
    description="LSTM-based Stock Price Prediction with Trading Intelligence",
    version="1.0"
)

# ==============================
# ✅ CORS CONFIGURATION (IMPORTANT)
# ==============================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development. In production, restrict this.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class StockSymbolInput(BaseModel):
    stock_symbol: str




@app.get("/")
def health_check():
    return {
        "status": "API is running ✅",
        "model_loaded": True,
        "service": "AI Stock Market Prediction API"
    }


@app.get("/model-info")
def model_info():
    return {
        "model_type": "LSTM Neural Network",
        "input_sequence_length": 60,
        "features_used": ["Close Price"],
        "prediction_type": "Next-day closing price",
        "framework": "TensorFlow + FastAPI",
        "scaler": "MinMaxScaler",
        "data_source": "Yahoo Finance"
    }




@app.post("/predict")
def predict_stock(data: StockSymbolInput):
    try:
        stock_symbol = data.stock_symbol.upper().strip()

        # 🔍 Fetch 6 months of stock data
        stock_data = yf.download(stock_symbol, period="6mo")

        if stock_data.empty:
            raise HTTPException(
                status_code=404,
                detail="Invalid stock symbol or no data found"
            )

        # 📊 Extract last 60 closing prices
        closing_prices = stock_data["Close"].dropna().tail(60).values

        if len(closing_prices) < 60:
            raise HTTPException(
                status_code=400,
                detail="Not enough historical data (Need at least 60 days)"
            )

        # 🤖 Predict next price
        predicted_price = float(predict_next_price(closing_prices))
        current_price = float(closing_prices[-1])

        # 📈 Trading intelligence calculations
        target = predicted_price * 1.02
        stop_loss = predicted_price * 0.98

        trend = "Bullish 📈" if predicted_price > current_price else "Bearish 📉"
        profit_percent = ((predicted_price - current_price) / current_price) * 100

        # 📉 Risk analysis using volatility
        volatility = np.std(closing_prices)

        if volatility < 10:
            risk_level = "Low Risk 🟢"
        elif volatility < 30:
            risk_level = "Medium Risk 🟡"
        else:
            risk_level = "High Risk 🔴"

        # 📦 Final JSON Response
        return {
            "stock_symbol": stock_symbol,
            "analysis": {
                "current_price": round(current_price, 2),
                "predicted_price": round(predicted_price, 2),
                "trend": trend,
                "expected_profit_percent": round(profit_percent, 2),
                "suggested_target": round(target, 2),
                "suggested_stop_loss": round(stop_loss, 2),
                "risk_level": risk_level
            },
            "model_details": {
                "sequence_length": 60,
                "algorithm": "LSTM",
                "data_source": "Yahoo Finance"
            }
        }

    except HTTPException as http_error:
        raise http_error

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))