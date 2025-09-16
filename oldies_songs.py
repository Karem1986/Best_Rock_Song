from flask import Flask, render_template_string, send_from_directory
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

app = Flask(__name__)

# PostgreSQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

db = SQLAlchemy(app)

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
