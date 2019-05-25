import falcon
import subprocess

from .user import UserApi, UserAuth

def create_app(test=False):
	user_repo = 'localhost:50052'
	
	api = falcon.API()
	api.add_route('/api/v1/user/register', UserApi(user_repo, test))
	api.add_route('/api/v1/user/auth', UserAuth(user_repo, test))
	return api


def get_app():
    return create_app()