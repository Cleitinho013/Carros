from database import criar_banco
from models import Marca, Carro


def inserir_marca(session):
    print("\n--- CADASTRAR MARCA ---")

    nome = input("Nome da marca: ")
    pais = input("País: ")
    ano_fundacao = int(input("Ano de fundação: "))
    tipo = input("Tipo: ")

    marca = Marca(
        nome=nome,
        pais=pais,
        ano_fundacao=ano_fundacao,
        tipo=tipo
    )

    session.add(marca)
    session.commit()

    print("Marca cadastrada com sucesso!")


def listar_marcas(session):
    print("\n--- MARCAS ---")

    marcas = session.query(Marca).all()

    if not marcas:
        print("Nenhuma marca cadastrada.")
        return

    for marca in marcas:
        print(
            f"ID: {marca.id} | "
            f"Nome: {marca.nome} | "
            f"País: {marca.pais} | "
            f"Fundação: {marca.ano_fundacao} | "
            f"Tipo: {marca.tipo}"
        )


def excluir_marca(session):
    listar_marcas(session)

    try:
        id_marca = int(
            input("\nID da marca que deseja excluir: ")
        )
    except ValueError:
        print("ID inválido.")
        return

    marca = session.get(Marca, id_marca)

    if not marca:
        print("Marca não encontrada.")
        return

    session.delete(marca)
    session.commit()

    print("Marca excluída com sucesso!")


def inserir_carro(session):
    print("\n--- CADASTRAR CARRO ---")

    marcas = session.query(Marca).all()

    if not marcas:
        print("Cadastre uma marca primeiro.")
        return

    listar_marcas(session)

    try:
        marca_id = int(input("\nID da marca: "))
        ano = int(input("Ano: "))
        preco = float(input("Preço: "))
    except ValueError:
        print("Valor inválido.")
        return

    modelo = input("Modelo: ")
    placa = input("Placa: ")

    marca = session.get(Marca, marca_id)

    if not marca:
        print("Marca não encontrada.")
        return

    carro = Carro(
        modelo=modelo,
        ano=ano,
        placa=placa,
        preco=preco,
        marca_id=marca_id
    )

    session.add(carro)
    session.commit()

    print("Carro cadastrado com sucesso!")


def listar_carros(session):
    print("\n--- CARROS ---")

    carros = session.query(Carro).all()

    if not carros:
        print("Nenhum carro cadastrado.")
        return

    for carro in carros:
        print(
            f"ID: {carro.id} | "
            f"Modelo: {carro.modelo} | "
            f"Ano: {carro.ano} | "
            f"Placa: {carro.placa} | "
            f"Preço: R$ {carro.preco:.2f} | "
            f"Marca: {carro.marca.nome}"
        )


def excluir_carro(session):
    listar_carros(session)

    try:
        id_carro = int(
            input("\nID do carro que deseja excluir: ")
        )
    except ValueError:
        print("ID inválido.")
        return

    carro = session.get(Carro, id_carro)

    if not carro:
        print("Carro não encontrado.")
        return

    session.delete(carro)
    session.commit()

    print("Carro excluído com sucesso!")


def menu(session):

    while True:

        print("\n==============================")
        print("       SISTEMA DE CARROS")
        print("==============================")
        print("1 - Inserir marca")
        print("2 - Listar marcas")
        print("3 - Excluir marca")
        print("4 - Inserir carro")
        print("5 - Listar carros")
        print("6 - Excluir carro")
        print("7 - Trocar banco")
        print("0 - Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ")

        try:

            if opcao == "1":
                inserir_marca(session)

            elif opcao == "2":
                listar_marcas(session)

            elif opcao == "3":
                excluir_marca(session)

            elif opcao == "4":
                inserir_carro(session)

            elif opcao == "5":
                listar_carros(session)

            elif opcao == "6":
                excluir_carro(session)

            elif opcao == "7":
                session.close()
                return "trocar"

            elif opcao == "0":
                session.close()
                return "sair"

            else:
                print("Opção inválida.")

        except Exception as erro:
            session.rollback()
            print(f"Erro: {erro}")


def escolher_banco():

    while True:

        print("\n==============================")
        print("       ESCOLHA O BANCO")
        print("==============================")
        print("1 - SQLite")
        print("2 - MySQL")
        print("0 - Sair")
        print("==============================")

        opcao = input("Escolha: ")

        if opcao == "0":
            print("Programa encerrado.")
            break

        if opcao == "1":
            tipo_banco = "sqlite"

        elif opcao == "2":
            tipo_banco = "mysql"

        else:
            print("Opção inválida.")
            continue

        try:

            engine, Session = criar_banco(tipo_banco)

            session = Session()

            print(f"\nConectado ao {tipo_banco.upper()}!")

            resultado = menu(session)

            if resultado == "sair":
                break

        except Exception as erro:
            print(f"\nNão foi possível conectar: {erro}")


if __name__ == "__main__":
    escolher_banco()