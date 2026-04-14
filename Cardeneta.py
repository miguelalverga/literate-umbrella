# Tipo Abstrato de Dado (TAD) 'Cardeneta'
# Lista sequencial dinâmica de alunos

# ATRIBUTOS:
class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

    def __repr__(self):
        return f"Aluno({self.matricula}, {self.nome})"

Cardeneta = []

# INTERFACE:
def insereNoFim(al, ct=Cardeneta):
    ct.append(al)

def posicaoAluno(matricula, ct=Cardeneta):
    matriculas = [al.matricula for al in ct]
    if matricula not in matriculas:
        return None
    return matriculas.index(matricula)

def removeAluno(pos, ct=Cardeneta):
    if 0 <= pos < len(ct):
        return ct.pop(pos)
    else:
        return None

def acessaAluno(pos, ct=Cardeneta):
    if 0 <= pos < len(ct):
        return ct[pos]
    else:
        return None

def NovoAluno(matricula=None, nome=None):
    # Se matrícula e nome não são fornecidos, solicita do usuário
    if not matricula:
        matricula = input("Digite a matrícula: ")
    if not nome:
        nome = input("Digite o nome do aluno: ")
    return Aluno(matricula, nome)

def EscreveAluno(aluno):
    if aluno:
        print(f"Matrícula: {aluno.matricula}, Nome: {aluno.nome}")
    else:
        print("Aluno não encontrado.")

# Teste Cardeneta
Cdta = Cardeneta
# Inserir um aluno com matrícula especificada para testes
insereNoFim(NovoAluno(matricula="2024G0741", nome="João Silva"), Cdta)
print("Tamanho atual da lista:", len(Cdta))

# Buscar aluno por matrícula
indice = posicaoAluno('2024G0741', Cdta)
print("Índice:", indice)

# Acessar e imprimir aluno pelo índice, se encontrado
if indice is not None:
    alunoBuscado = acessaAluno(indice, Cdta)
    EscreveAluno(alunoBuscado)
else:
    print("Matrícula não encontrada.")
