# Função para verificar se um caractere é uma consoante
def is_consoante(c):
    c = c.lower()  # Tornar minúsculo para facilitar a comparação
    return c.isalpha() and c not in 'aeiou'

# Inicializando a lista para armazenar os caracteres
vetor = []

# Lendo 10 caracteres
for i in range(10):
    char = input(f"Digite o {i+1}º caractere: ")
    vetor.append(char)

# Contando e imprimindo as consoantes
consoantes = [c for c in vetor if is_consoante(c)]
quantidade_consoantes = len(consoantes)

# Exibindo os resultados
print(f"Quantidade de consoantes: {quantidade_consoantes}")
print("Consoantes encontradas:", ', '.join(consoantes))
