from App.database import db
from App.models import *
class document(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     LearningOutcomes = db.Column(db.Integer, db.ForeignKey('LearningOutcomes.id'), nullable=False)
     assigment = db.Column(db.Integer, db.ForeignKey('Assigment.id'), nullable=False)
     rationale = db.Column(db.Integer, db.ForeignKey('Rationale.id'), nullable=False)
     content = db.Column(db.Integer, db.ForeignKey('Content.id'), nullable=False)
     resources = db.Column(db.Integer, db.ForeignKey('Resources.id'), nullable=False)
     stratigies = db.Column(db.Integer, db.ForeignKey('TeachingStratigies.id'), nullable=False)
     templateID = db.Column(db.Integer, db.ForeignKey('template.id'), nullable=False)
     name  = db.Column(db.String(120),nullable=False)

     def __init__(self,name):
          self.name = name