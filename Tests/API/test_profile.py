import pytest
import allure
from Profile_API import ProfileAPI
from Auth_API import create_otp, create_token_from_otp, refresh_token

@pytest.fixture
def valid_profile():
    return {
    "first_name": "Макс",
    "last_name": "Иванов",
    "language": "ru",
    "other_language": "en",
    "voice": "Female",
    "other_voice": "Female",
    "photo": None,
    "has_custom_voice": False
    }


@allure.feature("Profile")
@allure.story("Создание и удаление профиля")
def test_create_and_delete_profile(valid_profile):
    with allure.step("Получаем access_token"):
        otp = create_otp()
        tokens = create_token_from_otp(otp)
        new_tokens = refresh_token(tokens["refresh_token"])
        access_token = new_tokens["access_token"]

    with allure.step("Создаем профиль"):
        response = ProfileAPI.create_profile(valid_profile, access_token)
        assert response.status_code == 201, f"Профиль не создан: {response.text}"
        body = response.json()
        for key in valid_profile:
            assert body.get(key) == valid_profile[key], f"{key} не совпадает"

    with allure.step("Удаляем профиль"):
        delete_response = ProfileAPI.delete_my_profile(access_token)
        assert delete_response.status_code == 204, f"Удаление не удалось: {delete_response.text}"
