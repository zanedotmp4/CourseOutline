from App.models import RationaleTemp
from App.database import db

def create_RationaleTemp(text):
    rationaletemp = RationaleTemp(text=text)
    db.session.add(rationale)
    db.session.commit()
    return rationaletemp
    
