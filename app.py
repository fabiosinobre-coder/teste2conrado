from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])

def somar():
    valorA = 120
    valorB = 75
    return str(valorA + valorB)


if __name__ == "__main__":
    app.run()