from flask import Flask, jsonify, request

from lib.config import Config
from lib.picture_analizer import PictureAnalyzer

app = Flask(__name__)
config = Config()
picture_analyzer = PictureAnalyzer()


@app.route("/pictures", methods=["GET"])
def pictures():
    picture_analyzer.get_pictures(config.paths)
    return "test", 200


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
