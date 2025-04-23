# backend.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_script():
    data = request.json
    number = data.get("number")
    result = int(number) ** 2
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
