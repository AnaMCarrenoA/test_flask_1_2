from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"payload": "welcome to my project"})

@app.route("/put", methods=["PUT"])
def delete():
    return jsonify ({"payload":"put successfully"})

if __name__ == '__main__':
    app.run(debug=True)
