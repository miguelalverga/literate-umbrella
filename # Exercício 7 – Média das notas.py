# Leitura das 4 notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibindo as notas e a média
print(f"As notas foram: {nota1}, {nota2}, {nota3}, {nota4}")
print(f"A média das notas é: {media:.2f}")
