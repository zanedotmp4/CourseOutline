from App.models import Rationale,RationaleTemp
from App.database import db

def create_Rationale(text):
    rationale = Rationale(text=text)
    db.session.add(rationale)
    db.session.commit()
    return rationale

def get_template(id):
    template = db.session.query(RationaleTemp).filter(RationaleTemp.id == RationaleTemp.id).all()
    return template
