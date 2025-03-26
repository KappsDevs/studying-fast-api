from src.models import User, table_registry
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


def test_create_user(session):
    # engine = create_engine("sqlite:///database.db")
    # engine = create_engine("sqlite:///:memory:")
    # cria um banco de dado na memória -> é volátil
    #table_registry.metadata.create_all(engine)  # existe metadados dentro do banco


    user = User(username="nooome", email="emailo2@email.com", password="senha")

    session.add(user)
    # Adiciona na sessão
    session.commit()
    # Pegamos tudo que está na sessão e aí sim adicionamos no BD
    # session.refresh(user)
    # Atualizar especificamente o refresh -> sincroniza o que tem no banco com o que enviamos
    result = session.scalar(select(User).where(User.email == "emailo2@email.com"))

    assert result.username == "nooome"
