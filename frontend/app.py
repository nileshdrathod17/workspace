import json
import os
import urllib.request
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)
API_URL = os.getenv("API_URL", "http://localhost:5000")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Python DevOps Demo</title>
    <style>
        body { font-family: Arial; background: #f1f5f9;
               text-align: center; padding: 60px; }
        .card { background: white; padding: 30px;
                border-radius: 12px; max-width: 600px;
                margin: auto; box-shadow: 0 4px 15px #ddd; }
        h1 { color: #2563eb; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Python DevOps Demo</h1>
        <p>Frontend is running!</p>
        <h3>Backend response</h3>
        <p>{{ message }}</p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    try:
        with urllib.request.urlopen(API_URL + "/", timeout=3) as response:
            data = json.loads(response.read())
            message = data.get("message", "API available")
    except Exception:
        message = "Backend unavailable"
    return render_template_string(HTML, message=message)

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
