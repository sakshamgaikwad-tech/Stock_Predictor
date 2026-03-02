from tensorflow.keras.models import load_model
import joblib
import numpy as np

# Load trained model and scaler
model = load_model("models/lstm_model.h5")
scaler = joblib.load("models/scaler.save")


def predict_next_price(last_60_prices: list):
    """
    Predict next closing price using last 60 closing prices
    """

    if len(last_60_prices) != 60:
        raise ValueError("Exactly 60 closing prices are required")

    data = np.array(last_60_prices).reshape(-1, 1)

    # Scale data
    scaled = scaler.transform(data)

    # Reshape for LSTM (samples, timesteps, features)
    X = scaled.reshape(1, 60, 1)

    # Predict
    prediction = model.predict(X, verbose=0)

    # Convert back to original scale
    prediction = scaler.inverse_transform(prediction)

    return float(prediction[0][0])