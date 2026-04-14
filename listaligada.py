#ATRIBUTOS-----------------------------------
#Esta classe define um nó numa lista ligada
class NodoLista:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo =proximo_nodo
    def __repr__(self): #Define o objeto como uma string
        return '%s -> %s' % (self.dado, self.proximo)
#Esta classe cria uma lista ligada, definindo a cabeça da lista
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
    def __repr__(self):
        return("[" + str(self.cabeca) + "]") 
#INTERFACE----------------------------------------------------
def insere_no_inicio(lista, novo_dado):
    # 1) Cria um novo dado com o dado armazenado.
    novo_nodo = NodoLista(novo_dado)
    # 2) Faz com que o novo nodo seja a cabeça da Lista.
    novo_nodo.proximo = lista.cabeca
    # 3) Faz com que acabeça da lista referenciando o novo nodo
    lista.cabeca = novo_nodo
def insere_depois(lista, nodo_anterior, novo_dado):
    assert nodo_anterior, "Nodo anterior precisa existir na lista."
    # Cria um novo nodo com dado desejado.
    novo_dado.proximo = NodoLista(novo_dado)
    # Faz o próximo do novo dado ser próximo do nodo anterior.
    novo_dado.proximo = nodo_anterior.proximo
    # Faz com que o novo nodo seja o próximo do nodo anterior.
    nodo_anterior.proximo = novo_dado
def busca(lista, valor):
     corrente = lista.cabeca
     while corrente and corrente.dado != valor:
        corrente = corrente.proximo
        return corrente
def remove(self,valor):
    assert self.cabeca, "impossivel remover valor de lista vazia"
# Nodo a ser removido é a cabeca da lista
    if self.cabeca.dado == valor:
        self.cabeca = self.cabeca.proximo
    else:
        # Encontra a posição do elemento a ser removido.
        anterior = None
        corrente = self.cabeca
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo
        # o nodo corrente é o nodo a ser removido.
        if corrente:
            anterior.proximo = corrente.proximo
        else:
            # o nodo corrente é a cauda da lista.
            anterior.proximo = None
# IMPLEMENTAÇÃO DOS PONTEIROS E OBJETOS
# Implementação do método insere_no-INICIO
print('Teste')
lista = ListaEncadeada()
print('Lista vazia:', lista)
insere_no_inicio(lista, 5)
print("Lista contém um único elemento:", lista)
nodo_anterior = lista.cabeca
#Implementação do método insere_depois
insere_depois(lista, nodo_anterior, 10)
print("Inserindo um novo elemento depois de um outro:", lista)
print(lista.__sizeof__())
#Implementação do método busca
lista = ListaEncadeada()
for i in range(8):
    insere_no_inicio(lista, i)
print("Lista:", lista)
for i in range(8, -4, -2):
    elemento = busca(lista, i)
    if elemento:
        print("Elemento{0} presente na lista!".format(i))
    else:
        print("Elemento {0} não encontrado.".format(i))
print(lista.__sinzeof__())
# Implementação o método remove
lista = ListaEncadeada()
for i in range(5):
    insere_no_inicio(lista, i)
print("Lista:", lista)
print("Removendo elementos:")
for i in range(5):
    remove(lista, i)
    print("Removendo o elemento {0}: {1}".format(i, lista))
print(lista.__sinzof__())
