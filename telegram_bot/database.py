from data.users import User
from data import db_session
import hashlib


class DB:
    def create_user(self, user_id, username, mail, password):
        user = User()
        user.id = user_id
        user.name = username
        user.email = mail
        user.hashed_password = hashlib.md5(password.encode()).hexdigest()
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()

    def check_user(self, user_id):
        db_sess = db_session.create_session()
        return db_sess.query(User).filter(User.id == user_id).first()