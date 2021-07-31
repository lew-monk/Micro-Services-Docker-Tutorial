from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user", methods=["GET"])
def index():
    return jsonify("Print Send"), 200

if __name__ == "__main__":
    app.run(port=8000, debug=True)