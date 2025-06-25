from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    prompt = data.get('prompt')
    result = {
        "length": len(prompt),
        "uppercase": prompt.upper()
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
