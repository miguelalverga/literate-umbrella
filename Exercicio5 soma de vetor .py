v = int(input("Quantos números serão lidos:"))
somavetores = []
for i in range(v):
    somavetores.append(int(input()))
print(sum(somavetores))