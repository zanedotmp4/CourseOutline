from App.models import ResourcesTemp
from App.database import db
def create_ResourcesTemp(text):
    resoruces = ResourcesTemp(text=text)
    db.session.add(resoruces)
    db.session.commit()
    return resoruces