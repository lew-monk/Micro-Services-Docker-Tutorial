from flask import Flask, Response, json, request
import requests

app = Flask(__name__)

SITE_NAME = "http://localhost"


@app.route("/<path:path>/", methods=["GET","POST"])
def index(path):
    global SITE_NAME
    if request.method == "GET":
        if path == "video":
            port = 8001
            resp = requests.get(SITE_NAME + ":" + str(port) + "/" + path)
        else:
            port = 8000
            resp = requests.get(SITE_NAME + ":" + str(port) + "/" + path)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)

    else:
        if path == "video":
            port = 8001
            # print(SITE_NAME + ":" + str(port) + "/" + path, files=request.files)
            resp = requests.post(SITE_NAME + ":" + str(port) + "/" + path, files=request.files, data=request.form)
        else:
            port = 8000
            resp = requests.post(SITE_NAME + ":" + str(port) + "/" + path)
        
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
    return response



if __name__ == "__main__":
    app.run(port=80, debug=True)
