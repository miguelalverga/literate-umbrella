#ATRIBUTOS---------------------------------------
class clientes: #DECLARAR TIPO ABSTRATO AGENDA CLIENTES
     def __init__(self): # comando init serve para armazenar valores da variável
        self.nome = None # comando self serve para representar a instância da classe
        self.fone = '' # self permite que métodos acessem atributos
# DECLARAR VETOR CLIENTE
vetor_de_clientes = [{'nome': 'joaquin', 'fone': '888878654'},{'nome': 'joaquina','fone': '88994567'}]
# INTERFACE----------------------------------------------------------------------------------------------
def novoCliente(): # FUNÇÃO PARA REGISTRAR IM NOVO CLIENTE
    agenda = clientes
    agenda.nome = input("Digiteo nome do cliente:\n")
    agenda.fone = input("Digite o telefone do cliente:\n")
    vetor_de_clientes.append({'nome': agenda.nome, 'fone': agenda.fone})
    return agenda 
agenda = clientes
while True: # LAÇO PARA O PROGAMA CONTINUAR EXECUTANDO
    interface = int(input("""
 AGENDA TELEFÔNICA
1- Ver agenda                                                    
2- inserir Cliente
3- Encerrar                          
""")) # INTERFACE INTERATIVA
    if interface == 1: 
        for client in vetor_de_clientes:
            print('-------------------------------------------')
            print('Cliente')
            print('Nome: {client["nome"]}  Fone: {client["fone"][:5]}-{client["fone[:4]"]}')
    if interface == 2:
        novoCliente()
    if interface == 3:
        break # ENCERRA O LAÇO