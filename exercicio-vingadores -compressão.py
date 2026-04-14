vingadores = [ "Homemde Ferro ", "Capitão América", "Thor",  "Hulk", "Viúva Negra", "Gavião Aqueiro", ]
# adiciona "Homem-Aranha" usando contetenação de lista
vingadores = vingadores + ["Homem-Aranha"]
print(vingadores)
vingadores = [vingadores for vingadores in vingadores if vingadores != "Viúva Negra" and vingadores != "Homemde Ferro "  ]
print(vingadores)
print(vingadores[2])
x = (input("Qual Vingador procurar?: "))
print(f"{x} é um vingador presente," if x in vingadores else f"{x}é vingador desaparecido") 


