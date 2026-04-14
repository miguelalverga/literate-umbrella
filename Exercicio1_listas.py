n = int(input("Quantos números serão lidos?:"))
lista = []
for i in range(n):
    lista.append(int(input()))
x = int(input("Qual número a procura?: "))
if x in lista:
    print(x, "pertecem a lista")
else:
    print(x, " não pertecem a lista")