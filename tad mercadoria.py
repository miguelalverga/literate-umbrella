# TAD mercadoria
# Implementação do tipo registro mercadoria

class Mercadoria:
    def __init__(self, cod=0, nome='', pc=1.0, pv=1.0):
        self.cod = cod
        self.nome = nome
        self.pc = pc
        self.pv = pv

    def lucro(self):
        lucro = (self.pv - self.pc) * 100.0 / self.pc
        return lucro

    def __str__(self):
        return (f"Código: {self.cod}\n"
                f"Denominação: {self.nome}\n"
                f"Lucro: {self.lucro():.1f}%")

# Interface ----------------------------
def nova_mercadoria():
    cod = int(input("Digite o código: "))
    nome = input("Digite a denominação: ")
    pc = float(input("Digite o preço de compra (R$): "))
    pv = float(input("Digite o preço de venda (R$): "))
    return Mercadoria(cod, nome, pc, pv)

# Teste do TAD mercadoria
if __name__ == "__main__":
    print("Teste do TAD mercadoria")
    print("Dados de uma mercadoria:")
    # Cria uma mercadoria
    merc = nova_mercadoria()
    print("-----------------")
    print(merc)