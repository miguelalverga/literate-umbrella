 #Cria a matriz com as médias dos alunos
turma = [[5.0,4.5,7.0,5.2,6.1],[2.1,6.5,8.0,7.0,0.7,],[8.6,7.0,9.1,8.7,9.3]]
print(turma)
#segunda nota do primeiro aluno
print(turma[0][1])
#quinta nota do terceiro aluno
print(turma[2][4])
#calcular a média
media = 0
#for para pecorrer as linhas
for i in range(3): #matriz com 3 linhas
#for para pecorrer as colunas
    for j in range(5): #matriz com 5 colunas
        media = media + turma[i][j]
media = media / 15
print(media)
# cria uma turma vazia
turma = []
for i in range(3): # cria matriz com 3 linhas
# cria uma linha vazia
 linha = []
for j in range(5): # cria matriz com 5 coluna
    # vai adicionando as notas da linha
    linha.append(float(input('Digite a nota[' + str(i) +',' +str(j) +']:')))
    # adicione a linha na matriz turma
    turma.append(linha)