# Tipo Abstrato cadastro
from TADmercadoria import *
#ATRIBUTOS:---------------------------
# Obs.: Os dados das mercadorias estarão num
# vetor a ser criado na operação "CriaCdastro()"

#interface:-------------------------------------------
def CriaCadastro(qt):
    cad = [mercadoria()]*qt #cria vetor local com merc
    for i in range(qt): #substitui merc lendo do teclado
        cad [i] = NovaMercadoria()
    return cad #devolve o vetor preenchido
def CalculaLucroMedio(cad):
    soma = 0.0
    qt = len(cad)#obtém a quantid. elementos de cadastro
    for i in range(qt): #calcula a soma de todos os lucros
        soma += LucroMercadoria(cad[i])
    return soma/qt #retorna a média aritmetica dos lucros
#-------------------------------------------------------------
#cria cadastro com 2 mercadorias
cad = CriaCadastro(2)
EscreveMercadoria(cad[0])
EscreveMercadoria(cad[1])
CalculaLucroMedio(cad)