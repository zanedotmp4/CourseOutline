from App.database import db
from App.models import user,document

class departmentMember(db.Model):
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    documentID = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)
    isHod = db.Column(db.Boolean, default = False)

    def isHOD(self):
        return self.isHOD
    def assignHOD(self):
        self.isHod = True
    def toJSON(self):
        return{
            'userID':self.userID,
            'isHod':self.isHod

        }
        