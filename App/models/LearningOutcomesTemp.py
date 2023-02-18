from App.database import db
from App.models import document,template
class LearningOutcomesTemp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    docId = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)
    templateid= db.Column(db.Integer, db.ForeignKey('template.id'), nullable=False)
    text = db.Column(db.String(120),nullable=False)

    def __init__(self,text):
        self.text = text
    def to_JSON(self):
        return{
            'id':self.id,
            'docID':self.docId,
            'templateID':self.templateid,

            'text':self.text
        }