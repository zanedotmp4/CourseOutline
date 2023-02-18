from App.models import DescriptionTemp
from App.database import db

def create_Rationale(text):
    descriptionTemp = DescriptionTemp(text=text)
    db.session.add(description)
    db.session.commit()
    return descriptionTemp
    
