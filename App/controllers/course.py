from App.models import course
from App.database import db
def create_Course(name,prereq,ctype,level,credits,faculty):
    Course = course(name=name,prerequities=prereq,ciurseType=ctype,level=level,credits=credits,faculty=faculty)
    db.session.add(Course)
    db.session.commit()
    return Course