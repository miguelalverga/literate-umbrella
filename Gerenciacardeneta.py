from Cardeneta import *

Cdta = Cardeneta  # Cdta é um nome compacto para "Cardeneta"

# Explicita que lista está sendo manipulada
while True:
    print('---------------------')
    print('(1) Inserir aluno')
    print('(2) Remover aluno')
    print('(3) Consultar lista')
    print('(4) Encerrar')
    opc = input('Digite sua opção > ')

    if opc == '1':
        print('Digite os dados do aluno:')
        insereNoFim(NovoAluno(), Cdta)  # Chama NovoAluno() sem parâmetros

    elif opc == '2':
        matricula = input('Digite a matrícula do aluno para remover: ')
        indice = posicaoAluno(matricula, Cdta)
        if indice is not None:
            print('Aluno removido:')
            removido = removeAluno(indice, Cdta)
            EscreveAluno(removido)
        else:
            print('--> Aluno inexistente!')

    elif opc == '3':
        matricula = input('Digite a matrícula do aluno para acessar: ')
        indice = posicaoAluno(matricula, Cdta)
        if indice is not None:
            print('Dados do aluno:')
            alunoAcessado = acessaAluno(indice, Cdta)
            EscreveAluno(alunoAcessado)
        else:
            print('--> Aluno inexistente!')

    elif opc == '4':
        print("Encerrando o programa.")
        break

    else:
        print('Opção inválida')
