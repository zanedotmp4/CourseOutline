from App.models import LearningOutcomesTemp
from App.database import db

def create_LearningOutcomes(text):
    outcomes = LearningOutcomesTemp(text=text)
    db.session.add(outcomes)
    db.session.commit()
    return outcomes
    
##maybe i should search for the template in here also