import falcon

from .user import User

def create_app(user_repo):
    users = User(user_repo)
    api = falcon.API()
    api.add_route('/users', users)
    return api


def get_app():
    #user_repo = UserRepo('.')
    return create_app(None)