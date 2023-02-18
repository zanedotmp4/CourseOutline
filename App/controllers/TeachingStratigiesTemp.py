from App.models import TeachingStratigiesTemp
from App.database import db
def create_TeachingStratigiesTemp(text):
    strats = TeachingStratigiesTemp(text=text)
    db.session.add(strats)
    db.session.commit()
    return strats