# test_persistencia.py
import pytest
from modelos import ProductoModel

def test_guardar_y_consultar_producto_en_bd(db_session):
    # 1. Crear instancia del modelo
    producto = ProductoModel(nombre="Laptop Gamer", precio=3500.0, stock=5)

    # 2. Persistir en la BD en memoria
    db_session.add(producto)
    db_session.commit()

    # 3. Consultar la BD
    producto_guardado = db_session.query(ProductoModel).filter_by(nombre="Laptop Gamer").first()

    # 4. Aserciones
    assert producto_guardado is not None
    assert producto_guardado.id is not None
    assert producto_guardado.precio == 3500.0