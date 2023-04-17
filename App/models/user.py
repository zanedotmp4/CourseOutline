from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    email =  db.Column(db.String(120), nullable=False)
    userType = db.Column(db.String,default=False)

    def __init__(self,password,email):
        self.email = email
        self.set_password(password)
    
    def getID(self):
        return self.id
    def toJSON(self):
        return{
            'id': self.id,
            'email':self.email,
        }
    def setType(self,type):
        userType = type
        

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

