# Atributos -----------------------------------------
class Vendedor:  # Implementar o TAD de vendedor
    def __init__(self, cod, nome, vendas):
        self.cod = cod 
        self.nome = nome 
        self.vendas = vendas

    def mostra_vendedor(self):  # Função para mostrar os dados do vendedor
        print("Código:", self.cod)
        print("Nome:", self.nome)
        print("Total de vendas em R$:", self.vendas)

# Função fora da classe para criar um novo vendedor
def novo_vendedor():  # Criar os atributos do vendedor
    cod = int(input("Digite o código do vendedor: "))
    nome = input("Digite o nome do vendedor: ")
    vendas = float(input("Digite o total de vendas em R$: "))
    return Vendedor(cod, nome, vendas)

# Lógica de execução
n = int(input("Digite a quantidade de vendedores: "))
vendedores = []
total_vendas = 0

for i in range(n):  # Lista todos os vendedores
    vendedor = novo_vendedor()
    vendedores.append(vendedor)
    total_vendas += vendedor.vendas

media_vendas = total_vendas / n
print("\nMédia de vendas da loja: R$", media_vendas)

# Seleciona o melhor vendedor
melhor_vendedor = vendedores[0]
for vendedor in vendedores:
    if vendedor.vendas > melhor_vendedor.vendas:
        melhor_vendedor = vendedor

print("\nMelhor vendedor:")
melhor_vendedor.mostra_vendedor()

# Imprime os vendedores que precisam de treinamento
print("\nVendedores que precisam de treinamento:")
for vendedor in vendedores:
    if vendedor.vendas < media_vendas:
        vendedor.mostra_vendedor()
