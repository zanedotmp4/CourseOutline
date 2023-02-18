from App.database import db
class AssigmentTemp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    docId = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)
    templateid= db.Column(db.Integer, db.ForeignKey('template.id'), nullable=False)
    coutcomesID = db.Column(db.Integer, db.ForeignKey('assigment.id'), nullable=False)
    text = db.Column(db.String(120),nullable=False)
    def __init__(self,text):
        self.text = text
    def to_JSON(self):
        return{
            'id':self.id,
            'docID':self.docId,
            'templateID':self.templateid,
            'learningOutcomes':self.outcomesID,
            'text':self.text
        }