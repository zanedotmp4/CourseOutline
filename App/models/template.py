from App.database import db
from App.models import AssigmentTemp,ContentTemp,DescriptionTemp,LearningOutcomesTemp,RationaleTemp,ResourcesTemp,TeachingStratigiesTemp,CalanderTemp
class template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    LearningOutcomes = db.Column(db.Integer, db.ForeignKey('learning_outcomes_temp.id'), nullable=False)
    assigment = db.Column(db.Integer, db.ForeignKey('assigment_temp.id'), nullable=False)
    rationale = db.Column(db.Integer, db.ForeignKey('rationale_temp.id'), nullable=False)
    content = db.Column(db.Integer, db.ForeignKey('content_temp.id'), nullable=False)
    resources = db.Column(db.Integer, db.ForeignKey('resources_temp.id'), nullable=False)
    stratigies = db.Column(db.Integer, db.ForeignKey('teaching_stratigies_temp.id'), nullable=False)
    name  = db.Column(db.String(120),nullable=False)
    
    def __init__(self,text):
        self.text = text