import requests


reqres_urls = [("https://reqres.in/api/users", 201, '{"name": "morpheus","job": "leader"}'),
               ("https://reqres.in/api/users/2", 200, '{"name": "morpheus","job": "zion resident"}'),
               ("https://reqres.in/api/users/2", 200, '{"name": "morpheus","job": "zion resident"}')]


def test_post_create_user():
    response = requests.post(reqres_urls[0][0], reqres_urls[0][2])
    assert response.status_code == reqres_urls[0][1], f"Test response : {response.status_code}"


def test_put_update_user():
    response = requests.put(reqres_urls[1][0], reqres_urls[1][2])
    assert response.status_code == reqres_urls[1][1], f"Test response : {response.status_code}"


def test_patch_update_user():
    response = requests.patch(reqres_urls[2][0], reqres_urls[2][2])
    assert response.status_code == reqres_urls[2][1], f"Test response : {response.status_code}"
