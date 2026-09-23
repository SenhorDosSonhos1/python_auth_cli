from app.models import User

def test_if_password_difference_confirm_password():
    user = User(
    "test",
    "test@email.com",
    "123456",
    "654321"
)