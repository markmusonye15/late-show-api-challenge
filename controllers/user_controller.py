from models.user import User, UserType
from db.database import db

def get_all_users():

    users = db.session.query(User).all()
    return [user.__dict__ for user in users]

def get_a_user_and_delete():
    user = db.session.query(User).filter_by(username='testuser').first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return f"User {user.username} has been deleted successfully."
    else:
        return "User not found."
    
def create_a_new_user(user: UserType):
    new_user = User.create(user)
    return new_user.__dict__
 