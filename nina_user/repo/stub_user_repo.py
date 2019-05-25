import grpc
import nina_user.rpc.repo_service_pb2_grpc as repo_service_pb2_grpc
import nina_user.rpc.repo_service_pb2 as repo_service_pb2

from nina_user.repo.user_repo import User

def build_user_request(user):
    return repo_service_pb2.User(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password)

def build_email_request(email):
    return repo_service_pb2.UserEmail(user_email=email)

def build_id_request(user_id):
    return repo_service_pb2.UserId(user_id=user_id)

def validate_user(user):
	if (len(user.name) == 0 and len(user.email) == 0 and len(user.password) == 0):
		user = None
	return user

def build_user_from_response(response_user):
	user = User()
	user.id = response_user.id
	user.name = response_user.name
	user.email = response_user.email
	user.password = response_user.password
	return validate_user(user)

class StubUserRepo:

	def __init__(self, service_address, test=False):
		channel = grpc.insecure_channel(service_address)
		self.stub = repo_service_pb2_grpc.RepoServiceStub(channel)
		self.test = test

	def save(self, user):
		response =  self.stub.Save(build_user_request(user))
		return build_user_from_response(response)

	def find_by_email(self, email):
		try:
			response =  self.stub.FindByEmail(build_email_request(email))
			return build_user_from_response(response)
		except:
			return None

	def find_by_id(self, user_id):
		response =  self.stub.FindById(build_id_request(user_id))
		return build_user_from_response(response)

	def reset_databse(self):
		if(self.test):
			self.stub.ResetDatabase(repo_service_pb2.Empty())