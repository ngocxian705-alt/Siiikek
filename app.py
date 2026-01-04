from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/jwt")
def jwt():
    uid = request.args.get("uid")
    password = request.args.get("password")

    if not uid or not password:
        return jsonify({"error": "missing uid or password"}), 400

    url = f"http://jwt.thug4ff.com/token?uid={uid}&password={password}"

    try:
        r = requests.get(url, timeout=10)
        data = r.json()

        # ❌ XÓA CREDIT Ở ĐÂY
        if isinstance(data, dict) and "credit" in data:
            del data["credit"]

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": "api_failed", "detail": str(e)}), 500

app.run(host="0.0.0.0", port=5000)

