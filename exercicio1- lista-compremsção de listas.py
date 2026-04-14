n = int(input("Quantos números serão lidos?:"))
lista = [int(input()) for i in range(n)]
x = int(input("Qual número procurar?:"))
print(f"{x} {'pertence' if x in lista else 'não pertece'} à lista")