from App.database import db
from App.models import user,template

class CELTMember(db.Model):
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    document = db.Column(db.Integer, db.ForeignKey('template.id'), nullable=False)


    def toJSON(self):
        return{
            'userID':self.userID,
            'isHod':self.isHod
        }