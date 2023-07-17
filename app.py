from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"payload": "welcome to my project"})

@app.route("/read?content=foo", methods=["DELETE"])
def read():
    return jsonify ({"payload":foo})

if __name__ == '__main__':
    app.run(debug=True)
