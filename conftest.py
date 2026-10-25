# conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


# Clase base declarativa para los modelos ORM
class Base(DeclarativeBase):
    pass

@pytest.fixture(scope="function")
def db_session():
    """Crea una base de datos en memoria limpia para cada prueba unitaria."""
    engine = create_engine("sqlite:///:memory:", echo=False)

    # Importar modelos para registrar metadatos antes de crear tablas
    Base.metadata.create_all(bind=engine)

    # Crear sesion de trabajo
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    yield session  # Entrega la sesion activa al test

    session.close()  # Cierra la sesion al terminar el test