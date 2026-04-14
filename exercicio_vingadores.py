vingadores = [ "Homemde Ferro ", "Capitão América", "Thor",  "Hulk", "Viúva Negra", "Gavião Aqueiro", ]
vingadores.append('Homem Aranha')
print(vingadores)
if  "Thor" in vingadores:
    print(vingadores.index("Thor"))
if  "Viúva Negra" in vingadores:
    vingadores.remove("Viúva Negra")
if  "Homemde Ferro " in vingadores:
    vingadores.remove("Homemde Ferro ")
print(vingadores[2])
x = str(input("Procure um vingador: "))
if x in vingadores:
    print(x, "é um vingador")
else:
    print(x, "é um vingador desaparecido")