import json

import falcon
from nina_user.repo.user_repo import UserRepo, User

class UserApi:

    def __init__(self, user_repo):
        self.user_repo = user_repo

    def on_post(self, req, resp):
        #import ipdb
        #ipdb.set_trace(context=21)
        try:
            user_payload = json.load(req.bounded_stream)
            if(self.validate_user_payload(user_payload)):
                print user_payload
                new_user = User()
                new_user.name = user_payload['name']
                new_user.email = user_payload['email']
                new_user.password = user_payload['password']

                self.user_repo.save(new_user)

                resp_body = {
                    "status": "OK"
                }

                resp.body = json.dumps(resp_body, ensure_ascii=False)
        except:
            error_msg = {
                "status": "Bad Request"
            }
            resp.body = json.dumps(error_msg, ensure_ascii=False)
            resp.status = falcon.HTTP_BAD_REQUEST

    def validate_user_payload(self, user_data):
        if(user_data.has_key('name') and user_data.has_key('email') and user_data.has_key('password')):
            return True
        else:
            raise falcon.HTTPBadRequest()

class UserAuth:

    def __init__(self, user_repo):
        self.user_repo = user_repo

    def on_post(self, req, resp):
        pass