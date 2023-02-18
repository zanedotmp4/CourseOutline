from App.database import db
class update(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    prerequities = db.Column(db.String(120), nullable=True)
    courseType = db.Column(db.String(120), nullable=False)
    level = db.Column(db.String(120), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    faculty = db.Column(db.String(120), nullable=False)

    
    def __init__(self,name,courseType,level,credits,faculty,prerequities):
        self.name = name
        self.courseType = courseType
        self.level = level
        self.credits = credits
        self.faculty = faculty
        self.prerequities = prerequities
    def to_JSON(self):
        return{
            'id':self.id,
            'name':self.name,
            'prerequities':self.prerequities,
            'courseType':self.courseType,
            'level':self.level,
            'credits':self.credits,
            'faculty':self.faculty
        }