from App.models import ContentTemp
from App.database import db

def create_Rationale(text):
    contentTemp = ContentTemp(text=text)
    db.session.add(contentTemp)
    db.session.commit()
    return contentTemp
    
