from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize database connection and create table if not exists
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS data
                      (id INTEGER PRIMARY KEY, value TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/api/data', methods=['POST'])
def handle_data():
    data = request.json
    if 'value' in data:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO data (value) VALUES (?)", (data['value'],))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'}), 201
    return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(port=5001, debug=True)
