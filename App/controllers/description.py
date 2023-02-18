from App.models import description, DescriptionTemp
from App.database import db

def create_Rationale(text):
    description = description(text=text)
    db.session.add(description)
    db.session.commit()
    return description
    
def get_template(id):
    template = db.session.query(DescriptionTemp).filter(DescriptionTemp.id == description.id).all()
    return template