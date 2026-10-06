from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Marca(Base):
    __tablename__ = "marcas"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    pais: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    ano_fundacao: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    tipo: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    carros: Mapped[list["Carro"]] = relationship(
        back_populates="marca",
        cascade="all, delete-orphan"
    )


class Carro(Base):
    __tablename__ = "carros"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    modelo: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    ano: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    placa: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    preco: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    marca_id: Mapped[int] = mapped_column(
        ForeignKey("marcas.id"),
        nullable=False
    )

    marca: Mapped["Marca"] = relationship(
        back_populates="carros"
    )