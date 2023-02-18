from App.models import LearningOutcomes,LearningOutcomesTemp
from App.database import db

def create_LearningOutcomes(text):
    outcomes = LearningOutcomes(text=text)
    db.session.add(outcomes)
    db.session.commit()
    return outcomes
    
def get_template(id):
    template = db.session.query(LearningOutcomesTemp).filter(LearningOutcomesTemp.id == LearningOutcomes.id).all()
    return template