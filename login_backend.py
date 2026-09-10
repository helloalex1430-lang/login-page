from flask import Flask, request, jsonify, render_template
import datetime
import os

app = Flask(__name__, template_folder='templates')

# Path to the database file
DB_FILE_PATH = "users_database.txt"
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    mobile = data.get('mobile')
    password = data.get('password')
    pin = data.get('pin')
    
    login_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 # Path to the database file
if __name__ == '__main__':
    # Important: Create file with initial empty JSON object if it doesn't exist
    if not os.path.exists(DB_FILE_PATH):
        with open(DB_FILE_PATH, "w") as f:
            f.write("")
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
