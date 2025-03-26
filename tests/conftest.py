from fastapi.testclient import TestClient
from src.app import app
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    table_registry.metadata.create_all(engine)

    #gerenciamento de contexto
    with Session(engine) as session:
        yield session #tranfroma a session em gerador 

    table_registry.metadata.drop_all(engine)
