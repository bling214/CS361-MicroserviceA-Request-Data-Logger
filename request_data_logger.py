from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('requests.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS requests
                     (id INTEGER PRIMARY KEY,
                      time_taken REAL,
                      type TEXT,
                      timestamp TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/log', methods=['POST'])
def log_request():
    data = request.get_json()
    time_taken = data.get('time_taken')
    req_type = data.get('type')
    timestamp = datetime.now().isoformat()

    conn = sqlite3.connect('requests.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO requests (time_taken, type, timestamp) VALUES (?, ?, ?)",
                   (time_taken, req_type, timestamp))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success'}), 201

@app.route('/summary', methods=['GET'])
def summary():
    conn = sqlite3.connect('requests.db')
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(time_taken), COUNT(*) FROM requests")
    avg_time, total_requests = cursor.fetchone()
    conn.close()

    return jsonify({'average_time': avg_time, 'total_requests': total_requests})

@app.route('/delete', methods=['DELETE'])
def delete_all():
    conn = sqlite3.connect('requests.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM requests")
    conn.commit()
    conn.close()

    return jsonify({'status': 'all records deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True) # Flask defaults to port=5000
