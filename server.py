from flask import Flask, jsonify, request

from lib.config import Config

app = Flask(__name__)
config = Config()


@app.route("/pictures", methods=["GET"])
def pictures():
    pass


@app.route("/config", methods=["GET"])
def get_config():
    return jsonify(config.paths)


@app.route("/config", methods=["POST"])
def update_config():
    body = request.json
    if "paths" not in body:
        return "Required paths param not present in body", 400
    config.paths = body["paths"]
    return "Configuration updated", 200


