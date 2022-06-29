import requests


base_url = "http://localhost:8080/Plone/++api++"

username = "admin"
password = "admin"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# Authenticate
response = requests.post(
    f"{base_url}/@login",
    headers=headers,
    json={
        "login": username,
        "password": password,
    }
)

if response.status_code == 200:
    token = response.json()["token"]
    headers["Authorization"] = f"Bearer {token}"
    print(f"Autenticado Token: {token}")
else:
    raise ValueError("Usuário e/ou senha inválidos.")
