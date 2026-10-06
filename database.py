import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base


load_dotenv()


def criar_engine(tipo_banco):

    if tipo_banco == "sqlite":
        return create_engine(
            "sqlite:///av5.db"
        )

    if tipo_banco == "mysql":

        host = os.getenv("host")
        usuario = os.getenv("usuario")
        senha = os.getenv("senha","")
        banco = os.getenv("banco")
        porta = os.getenv("porta")
        print(host)
        print(usuario)
        print(senha)
        print(banco)
        print(porta)   
        
        if not all([
            host,
            usuario,
            banco,
            porta
        ]):
            raise ValueError(
                "Configure os dados do MySQL no arquivo .env"
            )

        url = (
            f"mysql+pymysql://{usuario}:{senha}"
            f"@{host}:{porta}/{banco}"
        )

        return create_engine(url)

    raise ValueError("Banco inválido!")


def criar_banco(tipo_banco):

    engine = criar_engine(tipo_banco)

    Base.metadata.create_all(engine)

    Session = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False
    )

    return engine, Session
