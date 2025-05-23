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

def update_user(updated_user: dict) -> dict:
    with state.session as ses:
        user = (
            ses
            .query(Users)
            .filter(Users.id == updated_user['id'])
            .first()
        )

        if not user:
            return None
        
        user.name = updated_user['name']
        user.password = updated_user['password']
        user.info = updated_user['info']
        ses.commit()
        return user.to_dict()
