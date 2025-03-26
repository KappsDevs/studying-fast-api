from sqlalchemy.orm import registry, Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime

# models.py -> modelos do banco de dados
# qual o nome da tabela, nomes dos campos da tabela, dos tipos
# schemas != model -> shema -> só o esqueleto

# registry - registra metadados(nome do campo)

table_registry = registry()
# mesma coisa que o declarative base

# Banco de dados tem tipos diferentes dos tipos de python
# Session -> atua como intermediário entre Python e o banco de dados


# classe de dados
@table_registry.mapped_as_dataclass()  # estrutura de python de dados
class User:
    __tablename__ = "users"  # objeto

    # init=False -> não precisamos inicializar, responsabilidade do banco
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
