#Atributos-----------------------------------------
class Vendedor: #implementar; o; TAD; de; vendedor;
    def __init__(self, cod, nome, vendas):
        self.cod = cod 
        self.nome = nome 
        self.vendas =vendas

    def novoVendedor(): #criar os  atributos
        cod = int(input("Digite o código do vendedor: "))
        nome = input("Digite o nome do vendedor: ")
        vendas = float(input("Digite o total de venndas em R$: "))
        return Vendedor(cod,nome, vendas)

#INTERFACE------------------------------------------------------
    def mostraVendedor(self): #criar as fenções
        print("Código:",self.cod)
        print("Nome: ",self.nome)
        print("Total de vendas em R$: ", self.vendas)

n = int(input("Digite a quantidade de vendedores: "))
vendedores = []
total_vendas = 0

for i in range(n): #lista todos os vendedor
    vendedor = Vendedor.novoVendedor()
    vendedores.append(vendedor)
    total_vendas += vendedor.vendas

media_vendas = total_vendas/n 
print("Média de vendas da loja: R$",media_vendas)

melhor_vendedor = vendedores[0]#selecionar o melhor vendedor
for vendedor in vendedores:
    if vendedor.vendas > melhor_vendedor.vendas:
        melhor_vendedor = vendedor

print("Melhor vendedor: ")#imprime na tela o melhor vendedor
melhor_vendedor.mostraVendedor()

print("Vendedores que precisa de treinamento: ")
for vendedor in vendedores:
    if vendedor.vendas < media_vendas:
        vendedor.mostraVendedor()