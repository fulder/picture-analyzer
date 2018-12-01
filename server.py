from flask import Flask, jsonify, request

from lib.config import Config
from lib.picture_analizer import PictureAnalyzer

app = Flask(__name__)
config = Config()
picture_analyzer = PictureAnalyzer(config)


@app.route("/pictures", methods=["GET"])
def pictures():
    picture_analyzer.get_pictures()
    return "test", 200


@app.route("/config", methods=["GET"])
def get_config():
    return jsonify(config.get_paths())


@app.route("/config", methods=["POST"])
def add_config():
    body = request.json
    if "path" not in body:
        return "Required 'path' param not present in body", 400
    config.add_path(body["path"])
    return "Configuration updated", 200
