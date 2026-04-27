from flask import Flask, jsonify, render_template, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# 🔗 DÔLEŽITÉ: nastav správnu URL
OLLAMA_URL = "https://destination-nurses-brokers-tracker.trycloudflare.com/api/chat"
# ak beží lokálne:
# OLLAMA_URL = "http://localhost:11434"

# -------------------
# DATA (nechávame tvoje)
# -------------------
database = {
    'students': [
        {"id": 1, "name": "samuel", "surname": "martis", "img": ""},
        {"id": 2, "name": "andrej", "surname": "bucko", "img": ""},
        {"id": 3, "name": "rasto", "surname": "patak", "img": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Magnus_Carlsen_in_2025.jpg"},
        {"id": 4, "name": "martin", "surname": "cepcek", "img": ""},
        {"id": 5, "name": "peter", "surname": "marcin", "img": ""},
        {"id": 6, "name": "janko", "surname": "kral", "img": ""},
        {"id": 7, "name": "lubo", "surname": "feldek", "img": ""},
        {"id": 8, "name": "ivan", "surname": "lesnik", "img": ""},
        {"id": 9, "name": "jozef", "surname": "mrkvicka", "img": ""},
        {"id": 10, "name": "michal", "surname": "kolar", "img": ""}
    ]
}

# -------------------
# ROUTES
# -------------------

@app.route('/')
def home():
    return "Backend beží ✅"

@app.route('/students')
def list_students():
    return jsonify(database["students"])

@app.route('/students/<int:id>')
def find_student(id):
    student = database["students"][id - 1]
    return jsonify(student)

@app.route('/ai')
def ai_page():
    return render_template("ai.html")  # musí byť v /templates

# -------------------
# 🔥 HLAVNÝ CHAT ENDPOINT
# -------------------

@app.route('/chat', methods=['POST'])
def chat():
    try:
        r = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json=request.json,
            stream=True,
            timeout=120
        )

        def generate():
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk

        return Response(generate(), content_type="text/plain")

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


# -------------------

if __name__ == '__main__':
    app.run(debug=True)
