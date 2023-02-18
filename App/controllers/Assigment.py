from App.models import Assigment, AssigmentTemp
from App.database import db
def create_Resources(text):
    assigment = Assigment(text=text)
    db.session.add(assigment)
    db.session.commit()
    return assigment

def get_template(id):
    template = db.session.query(AssigmentTemp).filter(Assigment.id == AssigmentTemp.id).all()
    return template
