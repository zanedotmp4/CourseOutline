from App.models import AssigmentTemp
from App.database import db
def create_Resources(text):
    assigmentTemp = AssigmentTemp(text=text)
    db.session.add(assigmentTemp)
    db.session.commit()
    return assigmentTemp 