from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/http://zaheerz.pythonanywhere.com/', methods=['POST'])
def webhook():
    data = request.get_json()
    # Process the incoming data (e.g., handle messages, events, etc.)
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run()
