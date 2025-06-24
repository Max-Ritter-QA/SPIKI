import allure
from Tests.API.Auth_API import create_otp,create_token_from_otp,refresh_token,delete_user

@allure.feature("Auth API")
@allure.story("Create OTP")
def test_create_otp():
    code = create_otp()
    assert code is not None and isinstance(code, str)

@allure.feature("Auth API")
@allure.story("Create Token from OTP")
def test_create_token():
    code = create_otp()
    tokens = create_token_from_otp(code)
    assert tokens["access_token"] is not None and isinstance(tokens["access_token"], str)
    assert tokens["refresh_token"] is not None and isinstance(tokens["refresh_token"], str)

@allure.feature("Auth API")
@allure.story("Refresh Token")
def test_refresh_access_token():
    code = create_otp()
    tokens = create_token_from_otp(code)

    old_refresh_token = tokens["refresh_token"]
    old_access_token = tokens["access_token"]

    refreshed = refresh_token(old_refresh_token)

    new_access_token = refreshed["access_token"]
    new_refresh_token = refreshed["refresh_token"]


    assert new_refresh_token is not None and new_refresh_token != old_refresh_token
    assert new_access_token is not None and  new_access_token != old_access_token

@allure.feature("User API")
@allure.story("Delete Current User")
def test_delete_current_user():
    code = create_otp()
    token = create_token_from_otp(code)
    old_refresh_token = token["refresh_token"]

    refreshed = refresh_token(old_refresh_token)
    new_access_token = refreshed["access_token"]

    result = delete_user(new_access_token)
    assert result is True