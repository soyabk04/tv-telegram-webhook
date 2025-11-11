from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)

# 🔐 Secrets stored in Render dashboard → Environment Variables
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = str(os.getenv("CHAT_ID"))

@app.route('/')
def home():
    return "✅ TradingView ↔ Telegram Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    print("Received from TradingView:", data)

    # Extract message safely
    message = data.get('message', '⚠️ No message field received.')
    text = f"📊 <b>TradingView Alert</b>\n\n{message}"

    # Send to Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, json=payload)
    print("Telegram response:", response.text)

    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
