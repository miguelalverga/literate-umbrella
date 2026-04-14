def eh_consoante(c):
    return c.isalpha() and c.lower() not in 'aeiouáéíóúãõ'

vetor = []
consoantes = []

for i in range(10):
    caractere = input(f"Digite o {i+1}º caractere: ")
    vetor.append(caractere)

for c in vetor:
    if eh_consoante(c):
        consoantes.append(c)

print(f"\nQuantidade de consoantes: {len(consoantes)}")
print("Consoantes lidas:", ", ".join(consoantes))