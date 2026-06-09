from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "message": "DevSecOps Mini Platform is running",
        "status": "ok"
        })

@app.get("/health")
def health_check():
    return jsonify({
        "status": "healthy"
        })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)