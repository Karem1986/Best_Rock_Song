from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    artist = db.Column(db.String(120), nullable=True)
    genre = db.Column(db.String(200), nullable=False)
    filepath = db.Column(db.String(200), nullable=False)
    

    def __repr__(self):
        return f"<Song {self.title} by {self.artist}>"
