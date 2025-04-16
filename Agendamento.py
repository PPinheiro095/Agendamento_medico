from datetime import datetime

medicos = []
pacientes = []
agendamentos = []

def cadastrar_medico():
    nome = input("Nome do médico: ")
    especialidade = input("Especialidade: ")
    medicos.append({"nome": nome, "especialidade": especialidade})
    print(f"Médico {nome} cadastrado com sucesso.\n")

def cadastrar_paciente():
    nome = input("Nome do paciente: ")
    idade = input("Idade: ")
    pacientes.append({"nome": nome, "idade": idade})
    print(f"Paciente {nome} cadastrado com sucesso.\n")

def listar_medicos():
    print("Médicos cadastrados:")
    for i, m in enumerate(medicos):
        print(f"{i+1}. {m['nome']} - {m['especialidade']}")
    print()

def listar_pacientes():
    print("Pacientes cadastrados:")
    for i, p in enumerate(pacientes):
        print(f"{i+1}. {p['nome']} - {p['idade']} anos")
    print()

def agendar_consulta():
    if not medicos or not pacientes:
        print("É necessário ter pelo menos um médico e um paciente cadastrados.\n")
        return

    listar_medicos()
    id_medico = int(input("Escolha o número do médico: ")) - 1

    listar_pacientes()
    id_paciente = int(input("Escolha o número do paciente: ")) - 1

    data_str = input("Data da consulta (dd/mm/aaaa hh:mm): ")
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
        agendamentos.append({
            "medico": medicos[id_medico],
            "paciente": pacientes[id_paciente],
            "data": data
        })
        print("Consulta agendada com sucesso!\n")
    except ValueError:
        print("Formato de data inválido.\n")

def listar_agendamentos():
    if not agendamentos:
        print("Nenhuma consulta agendada.\n")
        return
    print("Consultas agendadas:")
    for a in agendamentos:
        print(f"{a['data'].strftime('%d/%m/%Y %H:%M')} - Dr(a). {a['medico']['nome']} com paciente {a['paciente']['nome']}")
    print()

def menu():
    while True:
        print("=== Sistema de Agendamento Médico ===")
        print("1. Cadastrar médico")
        print("2. Cadastrar paciente")
        print("3. Agendar consulta")
        print("4. Listar agendamentos")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_medico()
        elif escolha == "2":
            cadastrar_paciente()
        elif escolha == "3":
            agendar_consulta()
        elif escolha == "4":
            listar_agendamentos()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()
