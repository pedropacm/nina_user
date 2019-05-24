import falcon

from .user import UserApi, UserAuth
from nina_user.repo.user_repo import UserRepo

def create_app():
	user_repo = UserRepo()
	api = falcon.API()
	api.add_route('/api/v1/user/register', UserApi(user_repo))
	api.add_route('/api/v1/user/auth', UserAuth(user_repo))
	return api


def get_app():
    #user_repo = UserRepo('.')
    return create_app()