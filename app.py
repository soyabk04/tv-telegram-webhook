from flask import Flask, request
import requests, os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/')
def home():
    return "✅ TradingView ↔ Telegram Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'No message content')
    text = f"📊 TradingView Alert:\n{message}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={'chat_id': CHAT_ID, 'text': text})
    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
