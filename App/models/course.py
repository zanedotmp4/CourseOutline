from App.database import db
class update(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    prerequities = db.Column(db.String(120), nullable=True)
    courseType = db.Column(db.String(120), nullable=False)
    level = db.Column(db.String(120), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    faculty = db.Column(db.String(120), nullable=False)