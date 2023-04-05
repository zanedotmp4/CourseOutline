from App.database import db
from App.models import LearningOutcomes,Assigment,Rationale,Content,Resources,TeachingStratigies,Resources,template,Calander
class document(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     LearningOutcomes = db.Column(db.Integer, db.ForeignKey('learning_outcomes.id'), nullable=False)
     Assigment = db.Column(db.Integer, db.ForeignKey('assigment.id'), nullable=False)
     rationale = db.Column(db.Integer, db.ForeignKey('rationale.id'), nullable=False)
     content = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)
     resources = db.Column(db.Integer, db.ForeignKey('resources.id'), nullable=False)
     stratigies = db.Column(db.Integer, db.ForeignKey('teaching_stratigies.id'), nullable=False)
     templateID = db.Column(db.Integer, db.ForeignKey('template.id'), nullable=False)
     calander = db.Column(db.Integer, db.ForeignKey('Calander.id'), nullable=False)
     name  = db.Column(db.String(120),nullable=False)

     def __init__(self,name):
          self.name = name