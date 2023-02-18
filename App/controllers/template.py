from App.models import template
from App.database import db
def create_ResourcesTemp(text):
    Template = template(text=text)
    db.session.add(Template)
    db.session.commit()
    return Template

def get_Doc(name):
    return template.query_by_filter(name=name).first()

def delete_Doc(Doc):
    db.session.delete(Doc)
    db.session.commit()
    return doc.id