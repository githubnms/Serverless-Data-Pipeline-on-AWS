from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

API_URL = "https://z3xhrdnd2a.execute-api.us-east-1.amazonaws.com/prod/ingest"

HOME_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Serverless Pipeline - Ingest</title></head>
<body>
    <h2>Submit Customer Records</h2>
    <form action="/submit" method="post">
        <textarea name="records" rows="6" cols="50" placeholder="Enter one record per line"></textarea><br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HOME_PAGE)

@app.route('/submit', methods=['POST'])
def submit():
    raw_text = request.form.get('records', '')
    records = [line.strip() for line in raw_text.split('\n') if line.strip()]

    if not records:
        return jsonify({"error": "No records provided"}), 400

    response = requests.post(API_URL, json={"records": records})

    return jsonify({
        "status_code": response.status_code,
        "response": response.json()
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)