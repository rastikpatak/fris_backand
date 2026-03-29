from flask import Flask, jsonify

app = Flask(__name__)

database = {
    'students': [
        {"id": 1, "name": "samuel", "surname": "martis", "img": "data:image/webp;base64,UklGRtAMAABXRUJQVlA4IMQMAAD…aXjYzlRmBLbhHC7bMAeXYRFKK8LgHgHAMg54+qZBkE6OYAAAA"},
        {"id": 2, "name": "andrej", "surname": "bucko", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:AN…zd5q6xrMx8H-ytLFhiaVTPCzvMF435VHWdB80bF_mIdY&s=10"},
        {"id": 3, "name": "rasto", "surname": "patak", "img": ""},
        {"id": 4, "name": "martin", "surname": "cepcek", "img": " "},
        {"id": 5, "name": "peter", "surname": "marcin", "img": " "},
        {"id": 6, "name": "janko", "surname": "kral", "img": " "},
        {"id": 7, "name": "lubo", "surname": "feldek", "img": " "},
        {"id": 8, "name": "ivan", "surname": "lesnik", "img": " "},
        {"id": 9, "name": "jozef", "surname": "mrkvicka", "img": " "},
        {"id": 10, "name": "michal", "surname": "kolar", "img": " "}
]}

@app.route('/')
def list_students():
    return jsonify(database["students"])

@app.route('/students/<int:id>')
def find_student(id):
    student = database["students"][id - 1]
    return jsonify(student)
@app.route('/str')
def pusti_stranku():
    return (index.html)

if __name__ == '__main__':
    app.run(debug=True)
