import allure
from Tests.API.Auth_API import create_otp,create_token_from_otp,refresh_token,delete_user

# @allure.feature("Auth API")
# @allure.story("Create OTP")
# def test_create_otp():
#     code = create_otp()
#     assert code is not None and isinstance(code, str)

# @allure.feature("Auth API")
# @allure.story("Create Token from OTP")
# def test_create_token():
#     code = create_otp()
#     token = create_token_from_otp(code)
#     assert token is not None and isinstance(token, str)
#
# @allure.feature("Auth API")
# @allure.story("Refresh Token")
# def test_refresh_access_token():
#     code = create_otp()
#     token = create_token_from_otp(code)
#     new_token = refresh_token(token)
#     assert new_token is not None and new_token != token

@allure.feature("User API")
@allure.story("Delete Current User")
def test_delete_current_user():
    code = create_otp()
    token = create_token_from_otp(code)
    new_token = refresh_token(token)
    result = delete_user(new_token)
    assert result is True