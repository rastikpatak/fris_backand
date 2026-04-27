import psycopg2

conn = psycopg2.connect(
    host="dpg-d7ng5n2qqhas73frva90-a/postgres_3eru",
    database="PostgreSQL",
    user="postgres_3eru_user",
    password="mOnYuHR6gLCRFzYhin9DSFpaTmd0lu9l",
    port="5432"
)

cursor = conn.cursor()
print("Pripojené!")
