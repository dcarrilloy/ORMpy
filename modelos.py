# modelos.py
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from conftest import Base

class ProductoModel(Base):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    precio: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, default=0)

    def aplicar_descuento(self, porcentaje: float) -> None:
        """Regla de negocio: Aplica un porcentaje de descuento al precio."""
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        self.precio -= self.precio * (porcentaje / 100.0)