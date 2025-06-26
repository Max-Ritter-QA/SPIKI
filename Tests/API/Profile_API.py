from config import BASE_URL
import requests

class ProfileAPI:
    endpoint = f"{BASE_URL}/api/v0/profiles/"

    @staticmethod
    def create_profile(payload: dict, token: str):
        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.post(
            ProfileAPI.endpoint,
            data=payload,
            headers=headers
        )
        return response

    @staticmethod
    def delete_my_profile(token: str):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        url = f"{BASE_URL}/api/v0/profiles/me"
        response = requests.delete(url, headers=headers)
        return response