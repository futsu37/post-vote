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
  

