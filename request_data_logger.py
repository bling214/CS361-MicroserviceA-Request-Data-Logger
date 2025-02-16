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
    try:
        data = request.get_json()
        if not data or 'time_taken' not in data or 'type' not in data:
            return jsonify({'error': 'Invalid input'}), 400

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
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/summary', methods=['GET'])
def summary():
    try:
        conn = sqlite3.connect('requests.db')
        cursor = conn.cursor()
        cursor.execute("SELECT AVG(time_taken), COUNT(*) FROM requests")
        avg_time, total_requests = cursor.fetchone()
        conn.close()

        if avg_time is None or total_requests is None:
            return jsonify({'average_time': None, 'total_requests': 0}), 200

        return jsonify({'average_time': avg_time, 'total_requests': total_requests}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete', methods=['DELETE'])
def delete_all():
    try:
        conn = sqlite3.connect('requests.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM requests")
        conn.commit()
        conn.close()

        return jsonify({'status': 'all records deleted'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) # Flask defaults to port=5000
