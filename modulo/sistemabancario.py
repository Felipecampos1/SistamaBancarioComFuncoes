#Nome: Felipe Campos
#Sistema Bancário Bootcamp Python Developer

import textwrap


def menu():
    menu = """\n
    \033[49;97m================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair
    => \033[m"""
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"\033[49;97mDepósito:\033[m\t\033[49;92mR$ {valor:.2f}\033[m\n"
        print("\n\033[49;96m$$$ Depósito realizado com sucesso! $$$\033[m")
        print(f'\033[49;97mSaldo:\033[m\033[49;92m R$ {saldo}\033[m')
    else:
        print("\n\033[49;91mOperação falhou! O valor informado é inválido.\033[m")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n\033[49;91mOperação falhou! Você não tem saldo suficiente.\033[m")

    elif excedeu_limite:
        print("\n\033[49;91mOperação falhou! O valor do saque excede o limite.\033[m")

    elif excedeu_saques:
        print("\n\033[49;91mOperação falhou! Número máximo de saques excedido.\033[m")

    elif valor > 0:
        saldo -= valor
        extrato += f"\033[49;97mSaque:\033[m\t\t\033[49;91mR$ -{valor:.2f}\033[m\n"
        numero_saques += 1
        print("\n\033[49;96m=== Saque realizado com sucesso! ===\033[m")
        print(f'\033[49;97mSaldo:\033[m \033[49;92mR$ {saldo}\033[m')

    else:
        print("\n\033[49;91mOperação falhou! O valor informado é inválido.\033[m")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n\033[49;97m================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n\033[49;97mSaldo:\033[m\t\t\033[49;92mR$ {saldo:.2f}\033[m")
    print("\033[49;97m==========================================\033[m")


def criar_usuario(usuarios):
    cpf = input("\033[49;97mInforme o CPF (somente número): \033[m")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\033[49;91mJá existe usuário com esse CPF!\033[m")
        return

    nome = input("\033[49;97mInforme o nome completo: \033[m")
    data_nascimento = input("\033[49;97mInforme a data de nascimento (dd-mm-aaaa): \033[m")
    endereco = input("\033[49;97mInforme o endereço (logradouro, nro - bairro - cidade/sigla estado): \033[m")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\033[49;92m=== Usuário criado com sucesso! ===\033[m")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\033[49;97mInforme o CPF do usuário:\033[m ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\033[49;96m=== Conta criada com sucesso! ===\033[m")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n\033[1;49;91mUsuário não encontrado, fluxo de criação de conta encerrado!\033[m")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
           \033[49;97m Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("\033[49;97mInforme o valor do depósito:\033[m"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("\033[49;97mInforme o valor do saque:\033[m"))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "6":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("\033[49;91mOperação inválida, por favor selecione novamente a operação desejada.\033[m")


main()