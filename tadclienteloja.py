#TAD cliente loja
#ATRIBUTOS------------------------------------
class Cliente: #define a TAD Cliente
    def __init__(self):
        self.nome = input("digite o nome do cliente: ")
        self.fone = input("digite o telefone do cliente: ")
#INTERFACE------------------------------------------------
def NovoCliente(): #cadastra novo cliente
    return Cliente()
def EscreveCliente(c): #pede a entrada de clientes
    print("Nome:", c.nome)
    print("Telefone:", c.fone)
def CriaAgenda(qt): #salva clientes na agenda
    agenda = []
    for i in range(qt):
        c = NovoCliente()
        agenda.append(c)
    return agenda
agenda = CriaAgenda(2)
for c in agenda:
    EscreveCliente(c)
#Insere uma quantidade de clientes para cadastrar
qt = int(input("digite a quantidade de clientes:"))
agenda = CriaAgenda(qt)