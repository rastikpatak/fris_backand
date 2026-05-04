import psycopg2

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

conn = psycopg2.connect(
    host="dpg-d7ng5n2qqhas73frva90-a.frankfurt-postgres.render.com",
    database="postgres_3eru",
    user="postgres_3eru_user",
    password="mOnYuHR6gLCRFzYhin9DSFpaTmd0lu9l",
    port="5432",
    sslmode="require"
)

cursor = conn.cursor()

for student in database["students"]:
    cursor.execute("""
        INSERT INTO students (id, name, surname, img)
        VALUES (%s, %s, %s, %s)
    """, (student["id"], student["name"], student["surname"], student["img"]))

conn.commit()

cursor.close()
conn.close()

print("Students inserted!")
