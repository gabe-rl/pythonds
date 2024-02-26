# Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3
import os

os.system('cls')

lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
multiplos_3 = []

for numero in lista:
    if numero % 3 == 0:

        multiplos_3.append(numero)


print(multiplos_3)

