#coletando número do usuário
print('-'*20, 'Programa da tabuada', '-'*20)
n = int(input('Digite o número a ser multiplicado: '))

for i in range (1,11):

    s = n*i

    print(f'{n} x {i} = {s}')

    