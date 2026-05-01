from . import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    url = db.Column(db.Text)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))