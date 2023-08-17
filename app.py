from flask import Flask, request, 

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"payload": "welcome to my project"})

@app.route("/put", methods=["PUT"])
def delete():
    return jsonify ({"payload":"put successfully"})
=======
@app.route("/read")
def read():
    un_usuario = request.args.get("content")

    if un_usuario == "alfa":
        return {"payload": content}
    else:  return "error de usuario"

@app.route("/create")
def create():
    un_usuario = request.args.post("content")

    if un_usuario == "bravo":
        return {"payload": content}
    else:  return "error de usuario"

@app.route("/init")
def init():
    un_usuario = request.args.get("content")

    if un_usuario == "charlie":
        return {"payload":content}
    else:  return "error de usuario"


if __name__ == '__main__':
    app.run(debug=True)
