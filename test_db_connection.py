from main_app import app
from backend.schema.dbmodels import db
from sqlalchemy import text

with app.app_context():
    try:
        db.session.execute(text("SELECT 1")) 
        print("✅ Database connection successful!")
    except Exception as e:
        print("❌ Database connection failed:")
        print(e)
