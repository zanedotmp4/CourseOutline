from App.database import db

class document(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     LearningOutcomes = db.Column(db.Integer, db.ForeignKey('LearningOutcomes.id'), nullable=False)
     Assigment = db.Column(db.Integer, db.ForeignKey('Assigment.id'), nullable=False)
     rationale = db.Column(db.Integer, db.ForeignKey('Rationale.id'), nullable=False)
     content = db.Column(db.Integer, db.ForeignKey('Content.id'), nullable=False)
     resources = db.Column(db.Integer, db.ForeignKey('Resources.id'), nullable=False)
     stratigies = db.Column(db.Integer, db.ForeignKey('TeachingStratigies.id'), nullable=False)