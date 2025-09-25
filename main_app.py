print("✅ Starting!")
from flask import Flask, render_template_string, send_from_directory, request, jsonify
import os
from dotenv import load_dotenv
# IMPORT SCHEMAS:
from backend.schema.dbmodels import db, Song, User, Favorite

load_dotenv()  # Load variables from .env

app = Flask(__name__)

@app.route("/test", methods=["GET"])
def test():
    return "Route works", 200

# PostgreSQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

db.init_app(app)

SONG_FOLDER = "songs"
SONGS = [f for f in os.listdir(SONG_FOLDER) if f.endswith(".mp3")]

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Oldies but Goodies</title>
  <style>
    body { font-family: sans-serif; text-align: center; padding: 2em; background: #fdf6e3; }
    h1 { font-size: 2em; margin-bottom: 1em; }
    .song { margin-bottom: 2em; }
    audio { width: 100%; max-width: 400px; }
  </style>
</head>
<body>
  <h1>🎶 Oldies but Goodies</h1>
  {% for song in songs %}
    <div class="song">
      <p><strong>{{ song }}</strong></p>
      <audio controls>
        <source src="/songs/{{ song }}" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
    </div>
  {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML, songs=SONGS)

@app.route("/songs/<path:filename>")
def serve_song(filename):
    return send_from_directory(SONG_FOLDER, filename)

# Get fallback to prevent hitting the wrong route endpoint
@app.route("/ping", methods=['GET'])
def ping():
  print("✅ /ping route registered")
  return jsonify({'message': 'pong'}), 200

@app.route("/signup", methods=["POST"])
def signup_post():
    print("✅ /signup POST route hit")
    # No data was being sent in the body of the request, that was causing the error: No method allowed. 
    data = request.get_json()
    print("📦 Received data:", data)

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing mandatory fields'}), 400

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'Username or email already exists'}), 409

    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


# # Route for sign up faalback
# @app.route("/signup", methods=["GET"])
# def signup_get():
#     return jsonify({"error": "Use POST method to register"}), 405

if __name__ == "__main__":
  print("✅ Flask app is starting")
  app.run(host="0.0.0.0", port=8080, debug=True)
