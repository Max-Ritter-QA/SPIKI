import requests
from config import BASE_URL,EMAIL

def create_otp():
    url = f"{BASE_URL}/api/v0/auth/password"
    payload = {"email": EMAIL}
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Ожидаемый статус код: {response.status_code}"
    return response.json().get("code")

def create_token_from_otp(code):
    url = f"{BASE_URL}/api/v0/auth/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {"username": EMAIL, "password": code}
    response = requests.post(url, data=payload,headers = headers)
    assert response.status_code == 200, f"Ожидаемый статус код: {response.status_code}"
    return response.json().get("refresh_token")

def refresh_token(token):
    url = f"{BASE_URL}/api/v0/auth/token/refresh"
    payload = {"refresh_token": token}
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Ожидаемый статус код: {response.status_code}"
    return response.json().get("access_token")

def delete_user(token):
    url = f"{BASE_URL}/api/v0/auth/accounts/me"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204, f"Ожидаемый статус код: {response.status_code}"
    return True