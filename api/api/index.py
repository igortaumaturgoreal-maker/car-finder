from flask import Flask, request, jsonify
from scraper import fetch_olx

app = Flask(_name_)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "online", "message": "Car Finder API funcionando!"})

@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("q", "")

    resultados = {
        "olx": fetch_olx(termo)
    }

    return jsonify(resultados)

def handler(event, context):
    return app(event, context)
