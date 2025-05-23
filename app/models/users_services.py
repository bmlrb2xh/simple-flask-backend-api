from app import state
from app.models.users import Users

def list_users() -> list[dict]:
    with state.session as ses:
        user_list = (
            ses
            .query(Users)
            .order_by(Users.id.desc())
            .all()
        )
        return [user.to_dict() for user in user_list]

def get_user(user_id: int) -> dict:
    with state.session as ses:
        user = (
            ses
            .query(Users)
            .filter(Users.id == user_id)
            .first()
        )

        if not user:
            return None
        
        return user.to_dict()

def create_user(
    name: str,
    password: str,
    age: int
) -> dict:
    with state.session as ses:
        user = Users(
            name = name,
            password = password,
            age = age
        )

        ses.add(user)
        ses.commit()
        return user.to_dict()
    
def delete_user(user_id: int) -> dict:
    with state.session as ses:
        user = (
            ses
            .query(Users)
            .filter(Users.id == user_id)
            .first()
        )

        if not user:
            return None
        
        ses.delete(user)
        ses.commit()
        return user.to_dict()

def set_name(user_id: int, name: str) -> dict:
    with state.session as ses:
        user = (
            ses
            .query(Users)
            .filter(Users.id == user_id)
            .first()
        )

        if not user:
            return None
        
        user.name = name
        ses.commit()
        return user.to_dict()
    
def set_password(user_id: int, password: str) -> dict:
    with state.session as ses:
        user = (
            ses
            .query(Users)
            .filter(Users.id == user_id)
            .first()
        )

        if not user:
            return None
        
        user.password = password
        ses.commit()
        return user.to_dict()

def set_info(user_id: int, info: str) -> dict:
    with state.session as ses:
        user = (
            ses
            .query(Users)
            .filter(Users.id == user_id)
            .first()
        )

        if not user:
            return None
        
        user.info = info
        ses.commit()
        return user.to_dict()
