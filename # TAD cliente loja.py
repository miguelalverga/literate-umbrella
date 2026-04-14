# TAD cliente loja
# ATRIBUTOS------------------------------------
class Cliente:  # Define a TAD Cliente
    def __init__(self):  # Corrected from _init_ to __init__
        self.nome = input("Digite o nome do cliente: ")
        self.fone = input("Digite o telefone do cliente: ")

# INTERFACE------------------------------------------------
def NovoCliente():  # Cadastra novo cliente
    return Cliente()

def EscreveCliente(c):  # Exibe dados do cliente
    print("Nome:", c.nome)
    print("Telefone:", c.fone)

def CriaAgenda(qt):  # Salva clientes na agenda
    agenda = []
    for i in range(qt):
        print(f"\nCadastro do Cliente {i+1}:")
        c = NovoCliente()
        agenda.append(c)
    return agenda

# Insere uma quantidade de clientes para cadastrar
qt = int(input("Digite a quantidade de clientes a cadastrar: "))
agenda = CriaAgenda(qt)

# Exibe os dados dos clientes cadastrados
print("\nClientes cadastrados:")
for c in agenda:
    EscreveCliente(c)