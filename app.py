from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/user')
def user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return str(result)

@app.route('/greet')
def greet():
    name = request.args.get('name')
    return f"<h1>Hello, {name}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
