"""
Crie um programa que permita ao usuário calcular a média de notas de um aluno.
O programa deve solicitar ao usuário que insira a quantidade de notas que
deseja calcular. Em seguida, o programa deve solicitar ao usuário que insira
cada uma das notas. Após inserir todas as notas, o programa deve calcular a
média e exibi-la na tela.
"""

qtd_notas = int(input('Qual a quantidade de notas que deseja calcular? '))
lista_notas = []
contador = 0
soma_notas = 0
print()
while contador < qtd_notas:
    nota = int(input(f'Informe a nota nº {contador+1}: '))
    lista_notas.append(nota)
    contador += 1

for i in lista_notas:
    soma_notas += i

media = soma_notas / qtd_notas
print(f'\nA média final das notas é: {media}')
