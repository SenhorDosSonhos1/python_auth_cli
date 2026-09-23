from app.security import get_password_hash, verify_password

def test_get_password__hash_not_return_plain_difference_password():
    assert get_password_hash("12346") != "12346"

def test_verify_password_hash_equal_return():
    result = get_password_hash("12346")
    assert verify_password("12346", result) == True

def test_verify_password_hash_different_return():
    result = get_password_hash("12346")
    assert verify_password("123", result) == False