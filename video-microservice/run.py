from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/video", methods=["GET", "POST"])
def video():

    print(request.form)
    # print(request.data)


    if "file" not in request.files:
        return jsonify("No Files Uploaded"), 500
    
    file = request.files['file']

    print(request.files)
    if file.filename == '':
        return jsonify('No image selected for uploading'), 400
        
    filename = secure_filename(request.form.get("email"))
    file.save(filename)
    return jsonify("Okay"), 200

if __name__ == "__main__":
    app.run(port=8001, debug=True)