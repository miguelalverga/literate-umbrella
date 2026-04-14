#TAD "cadastroloja"
from cadastro import *
qtde = int(input("digite a quantidade de mercadorias: "))
cad = Criacadastro(qtde)
LucroMedio = CalcularLucroMedio(cad)
print ("Mercadorias com lucro superior a média")
for merc in cad:
    if LucroMercadoria(merc) > LucroMedio:
        EscreveMercadoria(merc)