from App.database import db
class template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    