import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

@pytest.fixture
def client() -> TestClient: # type: ignore
  with TestClient(app) as client:
    yield client
