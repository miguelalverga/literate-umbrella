# Lista sequencial Dinâmica
# Tipo Absatrato 'Cardeneta'
#ATRIBUTOS:---------------------------
Cardeneta = []
#INTERFACE:----------------------------
def insereNoFim(al, ct = Cardeneta):
    ct.append(al)
def posicaoAluno(matricula, ct = Cardeneta):
    matriculas =[al.matric for al in ct]
    if matricula not in matriculas: return None
    return matriculas.index(matricula)
def removeAluno(pos, ct = Cardeneta):
    return ct.pop()
def acessaAluno(pos, ct = Cardeneta):
    return ct[pos]
print ('Teste cardeneta')
from lista_dinamica_aluno import *
Cdta = Cardeneta
insereNoFim(NovoAluno(),Cdta)
print (len(Cdta)) # conferir o tamanho atual da lista
indice = posicaoAluno('2024G0741, Cdta')
print (indice) # imprime indice ou se verifica:indice!=None
alunoBuscado = acessaAluno(indice, Cdta)
EscreveAluno(alunoBuscado)

