from flask import Flask, request
import requests, os

app = Flask(__name__)


BOT_TOKEN = os.getenv("8250719409:AAFWkaVoGoWZQwCG0LFXJLt4KwM8eYr3xGA")
CHAT_ID = os.getenv(6990746336)

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



