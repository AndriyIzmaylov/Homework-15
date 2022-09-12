import requests


reqres_urls = [("https://reqres.in/api/users", 200),
        ("https://reqres.in/api/users/2", 200),
        ("https://reqres.in/api/unknown/23", 404)]


def test_get_list_of_users():
    response = requests.get(reqres_urls[0][0])
    assert response.status_code == reqres_urls[0][1], f"Test response : {response.status_code}"


def test_get_user_by_id():
    response = requests.get(reqres_urls[1][0])
    assert response.status_code == reqres_urls[1][1], f"Test response : {response.status_code}"


def test_get_resource_not_found():
    response = requests.get(reqres_urls[2][0])
    assert response.status_code == reqres_urls[2][1], f"Test response : {response.status_code}"
