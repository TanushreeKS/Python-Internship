from . import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)

    
    videos = db.relationship('Video', backref='course', lazy=True)