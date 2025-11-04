from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def serve_index():
    return send_from_directory("web", "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory("web", path)

@app.route("/auto", methods=["POST"])
def auto_empfangen():
    data = request.get_json()
    marke = data.get("marke")
    ps = data.get("ps")
    verbrauch = data.get("verbrauch")

    antwort = {
        "status": "ok",
        "message": f"Auto '{marke}' mit {ps} PS und {verbrauch} L/100km wurde gespeichert."
    }

    # Terminal-Ausgabe
    print("=== Neue Anfrage erhalten ===")
    print(f"Marke: {marke}")
    print(f"PS: {ps}")
    print(f"Verbrauch: {verbrauch}")
    print(f"Antwort an Client: {antwort}")
    print("=============================\n")

    return jsonify(antwort)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

