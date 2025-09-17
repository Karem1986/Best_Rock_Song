# init_db.py
from oldies_songs import app
from backend.schema.dbmodels import db

with app.app_context():
    db.create_all()
    print("✅ All tables created successfully!")
