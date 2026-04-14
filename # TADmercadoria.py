# TADmercadoria.py
class TADMercadoria:
    def __init__(self, cod=0, nome='', pc=1.0, pv=1.0):
        self.cod = cod
        self.nome = nome
        self.pc = pc
        self.pv = pv

    def lucro(self):
        return (self.pv - self.pc) * 100.0 / self.pc

    def __str__(self):
        return (f"Código: {self.cod}\n"
                f"Denominação: {self.nome}\n"
                f"Preço de Compra: R$ {self.pc:.2f}\n"
                f"Preço de Venda: R$ {self.pv:.2f}\n"
                f"Lucro: {self.lucro():.1f}%")

def nova_mercadoria():
    cod = int(input("Digite o código: "))
    nome = input("Digite a denominação: ")
    pc = float(input("Digite o preço de compra (R$): "))
    pv = float(input("Digite o preço de venda (R$): "))
    return TADMercadoria(cod, nome, pc, pv)

def escreve_mercadoria(mc):
    print(mc)
    
# main.py
from TADmercadoria import *  # Ensure this file is named TADmercadoria.py and in the same directory

print("Teste do TAD mercadoria")
print("Dados de uma mercadoria:")

# Cria uma mercadoria
merc = nova_mercadoria()

print("----------------")
# Mostra os dados da mercadoria criada
escreve_mercadoria(merc)