import os
import requests
from flask import Flask, jsonify
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()
API_KEY = os.getenv("FINNHUB_API_KEY")

app = Flask(__name__)

@app.route('/quote/<symbol>', methods=['GET'])
def get_stock_quote(symbol):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch stock data"}), response.status_code

    data = response.json()
    return jsonify({
        "symbol": symbol,
        "open": data["o"],
        "high": data["h"],
        "low": data["l"],
        "current": data["c"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
