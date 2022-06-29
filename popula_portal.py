import requests


base_url = "http://localhost:8080/Plone/++api++"
username = "admin"
password = "admin"

headers = {"Accept": "application/json", "Content-Type": "application/json"}

# Authenticate
response = requests.post(
    f"{base_url}/@login",
    headers=headers,
    json={"login": username, "password": password},
)

if response.status_code == 200:
    token = response.json()["token"]
    headers["Authorization"] = f"Bearer {token}"
    print(f"Autenticado! Token: {token}")
else:
    raise ValueError("Usuário ou senha inválidos")

# Create content


def add_to_plone(path: str, payload: dict):
    url = f"{base_url}{path}"
    obj_id = payload["id"]
    obj_url = f"{url}/{obj_id}"
    response = requests.get(obj_url, headers=headers)
    if response.status_code == 404:
        # Content does not exist yet, create
        response = requests.post(
            url,
            headers=headers,
            json=payload,
        )
        if response.status_code > 299:
            print(f"ERROR: {response.text}")
            return
        data = response.json()
        path = data["@id"]
        print(f"Created {path}")
        url = f"{path}/@workflow/publish"
        requests.post(url, headers=headers)
    elif response.status_code in (200, 301, 302, 308):
        # Content exists
        data = response.json()
        review_state = data.get("review_state")
        obj_url = data["@id"]
        if review_state == "private":
            requests.post(f"{obj_url}/@workflow/publish", headers=headers)
            print(f"Published {obj_url}")
        response = requests.patch(
            obj_url,
            headers=headers,
            json=payload,
        )
        print(f"Updated {obj_url}")
    else:
        # oops
        print(f"ERROR: {url} {response.text}")


# Create campus
add_to_plone(
    path="/",
    payload={
        "@type": "Document",
        "id": "campus",
        "title": "Campus",
        "description": "Lista de Campus da UFT",
    },
)

# Create campus Palmas e Araguaína
contents = [
    # id, title, city
    ("palmas", "Palmas", "palmas"),
    ("araguaina", "Araguaína", "araguaina"),
]

for id_, title, city in contents:
    add_to_plone(
        path="/campus",
        payload={
            "@type": "campus",
            "id": id_,
            "title": title,
            "description": f"Campus da UFT em {title}",
            "city": city,
            "email": f"{city}@uft.edu.br",
        },
    )
