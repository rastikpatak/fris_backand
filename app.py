from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
database = {
    'students': [
        {"id": 1, "name": "samuel", "surname": "martis", "img": "http://www.gcm.sk/images/logo.jpg"},
        {"id": 2, "name": "andrej", "surname": "bucko", "img": "http://www.gcm.sk/images/logo.jpg"},
        {"id": 3, "name": "rasto", "surname": "patak", "img": "https://www.google.com/imgres?q=magnus%20carlson&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F1%2F1a%2FMagnus_Carlsen_in_2025.jpg&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMagnus_Carlsen&docid=2VArNktZpNYc6M&tbnid=7hkGYPak_LXjaM&vet=12ahUKEwj1zuiL__STAxW98LsIHcu2N6sQnPAOegQIHhAB..i&w=1558&h=1906&hcb=2&ved=2ahUKEwj1zuiL__STAxW98LsIHcu2N6sQnPAOegQIHhAB"},
        {"id": 4, "name": "martin", "surname": "cepcek", "img": " "},
        {"id": 5, "name": "peter", "surname": "marcin", "img": " "},
        {"id": 6, "name": "janko", "surname": "kral", "img": " "},
        {"id": 7, "name": "lubo", "surname": "feldek", "img": " "},
        {"id": 8, "name": "ivan", "surname": "lesnik", "img": " "},
        {"id": 9, "name": "jozef", "surname": "mrkvicka", "img": " "},
        {"id": 10, "name": "michal", "surname": "kolar", "img": " "}
]}

@app.route('/students')
def list_students():
    return jsonify(database["students"])

@app.route('/students/<int:id>')
def find_student(id):
    student = database["students"][id - 1]
    return jsonify(student)
@app.route('/str')
def pusti_stranku():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
