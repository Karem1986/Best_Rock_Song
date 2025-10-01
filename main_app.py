from flask import Flask, render_template_string, send_from_directory, request, jsonify, render_template, request, url_for, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
import os
from dotenv import load_dotenv

# IMPORT SCHEMAS:
from backend.schema.dbmodels import db, Song, Users, Favorite

load_dotenv()  # Load variables from .env

app = Flask(__name__)
# Enable flask_login with the secret key, without it login does not work.
app.secret_key = os.getenv("SECRET_KEY") or "dev-key"

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Load user for Flask-Login/Retrieve user by id
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# PostgreSQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
# First create the database!
db.init_app(app)
# Then create the tables!
with app.app_context():
    db.create_all()

# Create app routes
@app.route("/dashboard")
@login_required
def dashboard():
    SONG_FOLDER = "songs"
    SONGS = [f for f in os.listdir(SONG_FOLDER) if f.endswith(".mp3")]
    return render_template("dashboard.html", username=current_user.username, songs=SONGS)
  
@app.route("/songs/<path:filename>")
def serve_song(filename):
    return send_from_directory("songs", filename)

@app.route("/signup", methods=["POST"])
def signup_post():
    print("✅ /signup POST route hit")
    # No data was being sent in the body of the request, that was causing the error: No method allowed. 
    data = request.get_json()
    print("Sending data with curl in the body:", data)

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing mandatory fields'}), 400

    if Users.query.filter((Users.username == username) | (Users.email == email)).first():
        return jsonify({'error': 'Username or email already exists'}), 409

    user = Users(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201
  
# Login route
@app.route("/login", methods=["GET", "POST"])
def user_login():
    print("✅ /login route hit")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = Users.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")

# Protected dashboard route
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", username=current_user.username)

# Logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

if __name__ == "__main__":
  print("✅ Flask app is starting")
  app.run(host="0.0.0.0", port=8080, debug=True)
