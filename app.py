from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt, datetime

app = Flask(__name__)
CORS(app)

SECRET = "thug4ff"

@app.route("/")
def home():
    return "API OK"

@app.route("/jwt")
def jwt_api():
    uid = request.args.get("uid")
    password = request.args.get("password")

    if not uid or not password:
        return jsonify(error=True, msg="missing uid/password")

    token = jwt.encode(
        {"uid": uid, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)},
        SECRET,
        algorithm="HS256"
    )

    return jsonify({
        "uid": uid,
        "server": "VN",
        "token": token
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)