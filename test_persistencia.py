# test_persistencia.py
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

def test_aplicar_descuento_actualiza_precio_en_bd(db_session):
    producto = ProductoModel(nombre="Teclado Mecanico", precio=100.0, stock=10)
    db_session.add(producto)
    db_session.commit()

    # Aplicar regla de negocio (10% descuento)
    producto.aplicar_descuento(10.0)
    db_session.commit()

    producto_actualizado = db_session.query(ProductoModel).filter_by(id=producto.id).first()
    assert producto_actualizado.precio == 90.0