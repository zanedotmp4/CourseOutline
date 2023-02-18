from App.models import Content, ContentTemp
from App.database import db

def create_Rationale(text):
    content = Content(text=text)
    db.session.add(content)
    db.session.commit()
    return content

def get_template(id):
    template = db.session.query(ContentTemp).filter(Content.id == ContentTemp.id).all()
    return template
