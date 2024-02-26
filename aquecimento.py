#leitura de lista

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

#tamanho, minimo e máximo da lista

menor = min(lista)
maior = max(lista)
tamanho = len(lista)
soma = sum(lista)

print(f'A lista contém {tamanho} elementos. Sendo: {menor} o menor e {maior} o maior.')
print(f'A soma da lista é {soma}.')