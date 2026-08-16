from fastapi.testclient import TestClient
from httpx import Response
def test_login(client: TestClient):

  response: Response = client.post(
    "/login",
    data={
      "username":"Tom",
      "password":"Tom"
      }
    )
  
  assert response.status_code == 200
  
def test_current_user(client: TestClient):
    client.post(
    "/login",
    data={
      "username":"Tom",
      "password":"Tom"
      }
    )
    response: Response = client.get("/users/current")

    assert response.status_code == 200

def test_create_user(client: TestClient):
    response: Response = client.post(
    "/users",
    data={
      "username": "string",
      "display_name": "string",
      "email": "user@example.com",
      "password": "string"
      }
    )

    assert response.status_code == 201
