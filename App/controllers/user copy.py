from App.models import User,departMember,CELTmember
from App.database import db

def create_user(username, password,email,type,isHOD):
    if(type=="department"):
        newuser = departMember(username=username, password=password,email=email)
        if(isHOD==True):
            newuser.assignHOD()
    if(type=="CELT"):
        newuser = CELTmember(username=username, password=password,email=email)

    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toJSON() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    