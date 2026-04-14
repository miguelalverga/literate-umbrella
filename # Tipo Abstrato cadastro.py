# Tipo Abstrato cadastro
from TADmercadoria import *  # Importing from the TADMercadoria module

# Interface:-------------------------------------------
def CriaCadastro(qt):
    cad = [None] * qt  # Initialize a list of size 'qt'
    for i in range(qt):  # Fill the list with new mercadorias read from input
        cad[i] = nova_mercadoria()  # Correctly call the function 'nova_mercadoria'
    return cad  # Return the filled list

def CalculaLucroMedio(cad):
    soma = 0.0
    qt = len(cad)  # Get the number of elements in the cadastro (cad list)
    for i in range(qt):  # Calculate the sum of all profits
        soma += cad[i].lucro()  # Use the 'lucro()' method from TADMercadoria class
    return soma / qt  # Return the average profit

# Testing the code
cad = CriaCadastro(2)  # Create a list with two mercadorias
print("----------------")
EscreveMercadoria(cad[0])  # Display the first mercadoria
EscreveMercadoria(cad[1])  # Display the second mercadoria
print("----------------")
lucro_medio = CalculaLucroMedio(cad)  # Calculate the average profit
print(f"Lucro médio: {lucro_medio:.2f}%")
