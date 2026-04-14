# Inicializando os vetores
vetor = []
vetor_par = []
vetor_impar = []

# Lendo 20 números inteiros
for i in range(20):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)
    
    # Verificando se o número é par ou ímpar
    if num % 2 == 0:
        vetor_par.append(num)
    else:
        vetor_impar.append(num)

# Imprimindo os três vetores
print("\nVetor com todos os números:", vetor)
print("Vetor com os números pares:", vetor_par)
print("Vetor com os números ímpares:", vetor_impar)
