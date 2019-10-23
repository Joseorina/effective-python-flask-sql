from werkzeug.security import safe_str_cmp
from .user import User

users = [
    User(1, 'bob','asdf ')
]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    """
    Generate JWT token
    
    Arguments:
        username {[type]} -- [description]
        password {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    user = userid_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user
    
def identity(payload):
    """
    Authenticate an endpoint    
    Arguments:
        payload {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    user_id = payload['identity']
    return userid_mapping(user_id, None)