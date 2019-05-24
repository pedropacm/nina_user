import pytest

from nina_user.repo.user_repo import UserRepo, User

def test_create_user():
	user_repo = UserRepo()

	user = User()
	user.email = "test@example.com"
	user.password = "12345"

	user_repo.save(user)

	retrieved_user = user_repo.find_by_email("test@example.com")

	assert user.email == retrieved_user.email