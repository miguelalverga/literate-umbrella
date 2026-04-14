# Tipo abstrato "Aluno"
# Usando uma lista sequencia dinâmica
CH = 120.0 # Carga horária da diciplina
#ATRBUTOS---------------------------------
class Aluno: #implentação tipo registro aluno
    nome = ' '
    matric = ' '
    AB1 = 0.0
    AB2 = 0.0
    n_faltas = 0
# INTERFACE------------------------------------
def NovoAluno(): #criar um aluno em particular
    al = Aluno()
    al.nome = input('Nome: ')
    al.matric = input('Matricula: ')
    al.Ab1 = float(input('AB1: '))
    al.AB2 =float(input('AB2: '))
    al.n_faltas = int(input('Quant.faltas: '))
    return al
def Resultado(al): #determi9ne e retorna o resultado  do aluno
    global CH
    if al.n_faltas/CH > 0.25: return 'RF'
    media = (al.AB1 + al.AB2)/2
    if media >= 7.0: return 'AP'
    if media >= 5.0: return 'RA'
    return 'RM'
def EscreveAluno(al): #mostra um aluno em particular
    print('Nome: ', al.nome) 
    print('Matricula: ', al.matric)
    print('AB1: %.1f, AB2: %.1f' % (al.AB1, al.AB2))
    print('Num. faltas: ', al.n_faltas)
    print('Resultado: ', Resultado(al))
print ('Teste')
al = NovoAluno()
print (Resultado(al))
print(EscreveAluno(al))