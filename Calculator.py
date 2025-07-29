import os
import sqlite3
from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
# ⚠️ Hardcoded secret key (Security flaw)
app.secret_key = '12345supersecretkey'
 
# ⚠️ Database connection without context manager
def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn
 
# ⚠️ Insecure SQL query (SQL Injection possible)
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
 
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
 
    if user:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid credentials'})
 
# ⚠️ File upload with no security checks
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join('uploads', file.filename))
    return jsonify({'message': 'File uploaded'})
 
# ⚠️ Unused function and variable
def do_nothing(x):
    y = x * 2
    return None
 
# ⚠️ Logic error
@app.route('/divide', methods=['GET'])
def divide():
    a = int(request.args.get('a', 1))
    b = int(request.args.get('b', 0))  # Division by zero default
    result = a / b
    return jsonify({'result': result})
 
if __name__ == '__main__':
    # ⚠️ Debug mode on in production
    app.run(debug=True)
