from App.database import db
from App.models import AssigmentTemp,ContentTemp,DescriptionTemp,LearningOutcomesTemp,RationaleTemp,ResourcesTemp,TeachingStratigiesTemp,CalanderTemp
class template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    LearningOutcomes = db.Column(db.Integer, db.ForeignKey('LearningOutcomesTemp.id'), nullable=False)
    assigment = db.Column(db.Integer, db.ForeignKey('AssigmentTemp.id'), nullable=False)
    rationale = db.Column(db.Integer, db.ForeignKey('RationaleTemp.id'), nullable=False)
    content = db.Column(db.Integer, db.ForeignKey('ContentTemp.id'), nullable=False)
    resources = db.Column(db.Integer, db.ForeignKey('ResourcesTemp.id'), nullable=False)
    stratigies = db.Column(db.Integer, db.ForeignKey('TeachingStratigiesTemp.id'), nullable=False)
    calander = db.Column(db.Integer, db.ForeignKey('CalanderTemp.id'), nullable=False)
    name  = db.Column(db.String(120),nullable=False)
    
    def __init__(self,text):
        self.text = text