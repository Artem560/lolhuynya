from flask import Flask, request, jsonify
from pydantic import BaseModel, Field, ValidationError

app = Flask(__name__)

class MessageModel(BaseModel):
    message: str = Field(..., min_length=1, max_length=200)

@app.route('/')
def home():
    return """
<html>
<head><title>Startseite</title></head>
<body>
<h1>Willkommen!</h1>
<p>Der Server ist bereit und wartet auf Anfragen.</p>
<nav>
<a href="/profil">Profil</a> | 
<a href="/impressum">Impressum</a> |
<a href="/request-info">Request Info</a>
</nav>
</body>
</html>
    """


@app.route('/impressum')
def impressum():
    return """
<html>
<head><title>Impressum</title></head>
<body>
<h2>Impressum</h2>
<p>Dies ist ein Beispiel-Impressum.</p>
<p>Artem Kovtun</p>
<a href="/">Zurück zur Startseite</a>
</body>
</html>
    """


@app.route('/profil')
def profil():
    return """
<html>
<head><title>Profil</title></head>
<body>
<h2>Profil</h2>
<p>Name: Artem</p>
<p>Adresse: Bahnhofstr. 4 <br>50441 Köln</p>
<a href="/">Zurück zur Startseite</a>
</body>
</html>
    """


@app.route('/message', methods=['POST'])
def handle_message():
    try:
        input_data = request.get_json()
        if not input_data:
            raise ValueError("Keine JSON-Daten empfangen")

        msg = MessageModel(**input_data)
    except (ValidationError, ValueError) as e:
        return jsonify({"error": str(e)}), 400

    print(f"Empfangen: {msg.message}")
    response_message = f"Echo: {msg.message}"
    return jsonify({"response": response_message})


@app.route('/request-info', methods=['GET', 'POST'])
def request_info():
    info = {
        "Methode": request.method,
        "Query-Parameter (args)": request.args.to_dict(),
        "Formulardaten (form)": request.form.to_dict(),
        "JSON-Daten (json)": request.json if request.is_json else None,
        "Roher Body (data)": request.data.decode('utf-8'),
        "Header": dict(request.headers),
        "Cookies": request.cookies,
        "Pfad (path)": request.path,
        "Vollständige URL": request.url,
        "Client-IP": request.remote_addr
    }
    return jsonify(info)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)

