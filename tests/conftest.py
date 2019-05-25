from nina_user.repo.stub_user_repo import StubUserRepo

def pytest_runtest_setup(item):
	stub = StubUserRepo('localhost:50052', test=True)
	stub.reset_databse()
