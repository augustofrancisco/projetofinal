def funcao_buscar_cpf():
    cpf = int(input("Digite o CPF do cliente para consultar seus agendamentos:"))
    for i in lista_de_agendamentos:
        if i['cpf'] == cpf:
            l = lista_de_agendamentos.index(i)
            print(i)
        else:
            print("cpf invalido")

def func_todos_agend():
    print(lista_de_agendamentos)

def func_cancelar_agend():
    cpf = int(input("Digite o CPF do usuário p/ cancelar o agendamento:"))
    for i in lista_de_agendamentos:
        if i['cpf'] == cpf:
            l = lista_de_agendamentos.index(i)
            lista_de_agendamentos.remove(i)
            print("############################")
            print("Agendamento cancelado com sucesso!")
            print("############################")
            break
        else:
            print('CPF inválido')

lista_de_agendamentos = []

def func_agendamento():
    import calendar

    seu_cpf = int(input("Insira o CPF do cliente: "))
    ano_esc = int(input("\nAno: "))
    mes_esc = int(input("Mês: "))
    agenda = calendar.month(ano_esc, mes_esc)
    print("\n")
    print(agenda)
    dia_esc = int(input("\nDia: "))
    print("\nEscolha uma opcção: ")
    print("\n[1]07:00 às 08:00")
    print("[2]08:00 às 09:00")
    print("[3]10:00 às 11:00")
    print("[4]11:00 às 12:00")
    print("[5]14:00 às 15:00")
    print("[6]15:00 às 16:00")
    print("[7]16:00 às 17:00")
    horario_esc = int(input("\nHorário: "))

    dicionario_horarios = {}
    dicionario_horarios["Dia"] = dia_esc
    dicionario_horarios["Mes"] = mes_esc
    dicionario_horarios["Ano"] = ano_esc
    dicionario_horarios["Horario"] = horario_esc
    dicionario_horarios['cpf'] = seu_cpf

    lista_de_agendamentos.append(dicionario_horarios)

    print(dicionario_horarios)

    # dicionario_horarios = {}


lista_de_clientes = []


def identificador():
    import random
    chave_aleatoria = 10 * random.random() + cpf
    print("ID: %.3f" % (chave_aleatoria))


# Função Cadastro de clientes

def func_cadastro_cliente():
    while True:
        nome_completo = str(input("\nNome Completo: ")).title()
        if nome_completo == '':
            print('\nCampo obrigatório!')
            continue
        temp = ''.join(nome_completo.split(' '))
        for i in temp:
            if i.isdigit():
                print('Digite um nome válido.')
                continue
        else:
            break

    while True:
        data_nasc = str(input("\nData de Nascimento: "))
        if data_nasc == '':
            print('\nCampo obrigatório!')
        else:
            break

    while True:
        cpf = int(input("\nCPF: "))
        if cpf == '':
            print('\nCampo obrigatório!')
        else:
            break

    while True:
        estado_civil = str(input("\nEstado Civil: ")).title()
        if estado_civil == '':
            print('\nCampo obrigatório!')
        else:
            break

    while True:
        sexo = str(input("\nSexo: ")).title()
        if sexo == '':
            print('\nCampo obrigatório!')
        else:
            break

    while True:
        import random
        id_cliente = random.random() + cpf / 100 * 0.000037
        print("\nID: %.1f" % (id_cliente))
        print("\nCadastro realizado!")
        break

    # Dicionário para guardar o cadastro

    dicionario_clientes = {}
    dicionario_clientes["Nome"] = nome_completo
    dicionario_clientes["Data"] = data_nasc
    dicionario_clientes["CPF"] = cpf
    dicionario_clientes["Estado"] = estado_civil
    dicionario_clientes["Sexo"] = sexo
    dicionario_clientes["ID"] = id_cliente

    lista_de_clientes.append(dicionario_clientes)


# MENU

opcao = 0

while opcao != 6:
    print('\n')
    print("[1] Cadastrar Cliente")
    print("[2] Realizar Agendamento")
    print("[3] Cancelar Agendamento")
    print("[4] Cadastro de Serviços")
    print("[5] Relatórios")
    print("[6] Sair")

    opcao = int(input("\nInsira a Operação Desejada:"))

    if opcao == 1:
        func_cadastro_cliente()
    elif opcao == 2:
        print('\n')
        print("Defina uma Data: ")
        func_agendamento()
    elif opcao == 3:
        func_cancelar_agend()

    elif opcao == 5:
        cad = 0
        while cad != 5:
            print('[1] Relatório de Todos os Agendamentos')
            print('[2] Relatório de Agendamentos por Pessoa')
            print('[3] Relatório de Receita Total Por Mês')
            print('[4] Relatório Serviço Prestado por Pessoa')
            print('[5] Finalizar Consulta')
            cad = int(input('Selecione o relatório que deseja:'))
            if cad == 1:
                func_todos_agend()
            if cad == 2:
                funcao_buscar_cpf()
            '''if cad == 3:

            if cad == 4:'''








