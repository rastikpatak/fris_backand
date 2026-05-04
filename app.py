from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        host="dpg-d7ng5n2qqhas73frva90-a.frankfurt-postgres.render.com",
        database="postgres_3eru",
        user="postgres_3eru_user",
        password="mOnYuHR6gLCRFzYhin9DSFpaTmd0lu9l",
        port=5432,
    )

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

@app.route('/students/<int:id>', methods=["DELETE"])
def delete_student(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "deleted"})

if __name__ == "__main__":
    app.run(debug=True)
