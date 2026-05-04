from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from groq import Groq
import os

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

memory = {}

# DB
def get_db_connection():
    return psycopg2.connect(
        host="dpg-d7ng5n2qqhas73frva90-a.frankfurt-postgres.render.com",
        database="postgres_3eru",
        user="postgres_3eru_user",
        password="mOnYuHR6gLCRFzYhin9DSFpaTmd0lu9l",
        port= 5432,
    )

# ======================
# STUDENTS
# ======================

@app.route('/students', methods=["GET"])
def get_students():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, surname, personality, img FROM students")
    rows = cur.fetchall()

    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "name": r[1],
            "surname": r[2],
            "personality": r[3],
            "img": r[4]
        })

    cur.close()
    conn.close()
    return jsonify(result)

@app.route('/students', methods=["POST"])
def add_student():
    data = request.json

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO students (name, surname, personality, img)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """, (
        data["name"],
        data["surname"],
        data["personality"],
        data["img"]
    ))

    new_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": new_id})

@app.route('/students/<int:id>', methods=["PUT"])
def update_student(id):
    data = request.json

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE students
        SET name=%s, surname=%s, personality=%s, img=%s
        WHERE id=%s
    """, (
        data["name"],
        data["surname"],
        data["personality"],
        data["img"],
        id
    ))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "updated"})

@app.route('/students/<int:id>', methods=["DELETE"])
def delete_student(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id=%s", (id,))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "deleted"})

# ======================
# CHAT
# ======================

@app.route('/chat', methods=["POST"])
def chat():
    data = request.json

    name = data["name"]
    personality = data["personality"]
    message = data["message"]

    if name not in memory:
        memory[name] = []

    messages = [
        {
            "role": "system",
            "content": f"""
You are a student named {name}.
Personality: {personality}.
Speak short and natural.
"""
        }
    ]

    messages += memory[name]
    messages.append({"role": "user", "content": message})

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    reply = completion.choices[0].message.content

    memory[name].append({"role": "user", "content": message})
    memory[name].append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
