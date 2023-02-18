from App.models import Resources,ResourcesTemp
from App.database import db
def create_Resources(text):
    resoruces = Resources(text=text)
    db.session.add(resoruces)
    db.session.commit()
    return resoruces

def get_template(id):
    template = db.session.query(ResourcesTemp).filter(ResourcesTemp.id == Resources.id).all()
    return template