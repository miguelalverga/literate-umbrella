fucionarios = [] # lista vazia 
for i in range(4):
    fucionario = {} # registro de fucionario
    fucionario['nome'] = input("Digite o nome do fucionario%d: "%i)
    fucionario['salario'] = float(input("Digite o salário do fucionario %d: " % i))
    fucionarios.append(fucionario) # adicionar o dicionario a lista
for i in range(4):
    print("fucionario que ocupar a posição %d no vetor:" %i)
    print("Nome: %s" %fucionarios[i]['nome'])
    print("salario: R$ %.2f" % fucionarios[i]['salario'])