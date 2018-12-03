from flask import Flask, jsonify, request
from flask_cors import CORS
from lib.config import Config
from lib.picture_analizer import PictureAnalyzer

app = Flask(__name__)
CORS(app)
config = Config()
picture_analyzer = PictureAnalyzer(config)


@app.route("/pictures", methods=["GET"])
def pictures():
    ret = picture_analyzer.get_pictures()
    return jsonify(ret), 200


@app.route("/config", methods=["GET"])
def get_config():
    return jsonify(config.get_paths())


@app.route("/config", methods=["POST"])
def add_path():
    try:
        body = request.json
    except Exception:
        return "Couldn't parse body", 400

    if "path" not in body:
        return "Required 'path' param not present in body", 400

    config.add_path(body["path"])
    return "Configuration updated", 200
