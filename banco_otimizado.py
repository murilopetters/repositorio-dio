from operator import contains
import textwrap

def menu():
    menu_text = """\n
    ==============================   MENU  ============================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    [nu]\tNovo Usuario
    [nc]\tNova Conta
    [lc]\tLista de contas
    ===================================================================
    Comando => """
    return input(textwrap.dedent(menu_text))

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tR$ {valor:.2f}\n'
        print('\nDeposito realizado com sucesso !')
    else:
        print('\nOperação falhou! O valor informado é invalido.')
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('\nOperação falhou! Você não tem saldo suficiente.')
    elif excedeu_limite:
        print('\nOperação falhou! Você não tem limite suficiente.')
    elif excedeu_saques:
        print('\nOperação falhou! Número máximo de saques excedido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('Saque realizado com sucesso !')
    else:
        print('\nOperação falhou! O valor informado é inválido.')
    return saldo, extrato

def imprimir_extrato(saldo, /, *, extrato):
    print("============================== EXTRATO ==============================")
    print("Não foram realizadas movimentações na conta." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=====================================================================")

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente numeros): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('Já existe usuario com esse CPF: ')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, N - bairro - cidade/ sigla estado)')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuario registrado com sucesso !')

def filtrar_usuarios(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuario: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('\nConta criada com sucesso!')
        conta = {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
        contains.append(conta)
    else:
        print('\nUsuario não encontrado, fluxo de criação de conta encerrado: ')
    return conta if usuario else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do deposito: '))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == 'e':
            imprimir_extrato(saldo, extrato=extrato)
        elif opcao == 'nu':
            criar_usuario(usuarios)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'q':
            break
        else:
            print('Opção inválida, por favor selecione novamente uma opção válida.')

if __name__ == "__main__":
    main()