from App.models import TeachingStratigies
from App.database import db
def create_TeachingStratigies(text):
    strats = TeachingStratigies(text=text)
    db.session.add(strats)
    db.session.commit()
    return strats