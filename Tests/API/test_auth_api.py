import allure
from Auth_API import create_otp, create_token_from_otp, refresh_token, delete_user


@allure.feature("Auth API")
@allure.story("Полный цикл авторизации с удалением")
def test_full_auth_flow():
    with allure.step("Создание OTP (одноразового пароля)"):
        code = create_otp()
        assert code is not None and isinstance(code, str), "OTP должен быть строкой"

    with allure.step("Создание токенов (access и refresh) с помощью OTP"):
        tokens = create_token_from_otp(code)
        access_token = tokens["access_token"]
        refresh_tok = tokens["refresh_token"]

        assert access_token and isinstance(access_token, str), "access_token должен быть строкой"
        assert refresh_tok and isinstance(refresh_tok, str), "refresh_token должен быть строкой"

    with allure.step("Обновление токена (refresh_token -> новый access_token)"):
        refreshed_tokens = refresh_token(refresh_tok)
        new_access = refreshed_tokens["access_token"]
        new_refresh = refreshed_tokens["refresh_token"]

        assert new_access and new_access != access_token, "Новый access_token должен отличаться от старого"
        assert new_refresh and new_refresh != refresh_tok, "Новый refresh_token должен отличаться от старого"

    with allure.step("Удаление текущего пользователя"):
        result = delete_user(new_access)
        assert result.status_code == 204, f"Удаление пользователя не удалось: {result.status_code}, {result.text}"