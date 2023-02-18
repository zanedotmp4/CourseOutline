from App.models import document
from App.database import db

def create_document(name):
    newDoc = document(name=name)
    db.session.add(document)
    db.session.commit()
    return newDoc

def get_Doc(name):
    return document.query_by_filter(name=name).first()

def delete_Doc(Doc):
    db.session.delete(Doc)
    db.session.commit()
    return doc.id