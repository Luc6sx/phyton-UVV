N1 = int(input('Coloque um número aqui: '))
N2 = int(input('Coloque seu segundo número aqui: '))
print('OPRERAÇÕES ARITMETICAS BÁSICAS A SEGUIR')
print(f'Adição: N1 + N2 = {N1} + {N2} = {N1 + N2}')
print(f'Subtração: N1 - N2 = {N1} - {N2} = {N1 - N2}')
print(f'Multiplicação: N1 * N2 = {N1} * {N2} = {N1 * N2}')
print(f'Divisão: N1 + N2 = {N1} / {N2} = {N1 / N2}')
print(f'DIV (QUOCIENTE INTEIRO): N1 DIV N2 = {N1} // {N2} = {N1 // N2}')
print(f'MOD(RESTO INTEIRO): N1 % N2 = {N1} % {N2} = {N1 % N2}' )
print(f'POTENCIA: N1 ** N2 = {N1} ** {N2} = {N1 ** N2}')
print(f'RADICIAÇÃO: N1 ** (1 / N2) = {N1} ** {1 / N2:.1f} = {N1 ** (1 / N2): .1f}')

# PARTE 1 DA AULA
massa = float(input('Entre com sua massa (em KG):'))
altura = float(input('Entre com sua altura(EM METROS): '))

IMC = massa / (altura ** 2)

print(f'IMC (indice de massa corporea): {IMC: .2f}')

# Escrever um algoritmo em Python que leia de um (1) aluno sua nota do 1º e 2º bimestre
# e exiba na tela sua média semestral.

nomeAluno = str(input('Nome do Aluno:  '))
notaB1 = float(input(' nota do primeiro bimestre:  '))
notaB2 = float(input(' nota do seundo bimestre:   '))
notaTotal = (notaB1 + notaB2) / 2
print(f'media de nota do primerio e segundo bimesntre do {nomeAluno} é {notaTotal}')

# MEDIDA DE UMA BARRA

comprimento = float(input('MEDIDA DA BARRA EM CENTIMETROS'))
comprimento = comprimento / 2.54
print('MEDIAD DA BARRA:')
print(f'EM POLEGADAS: {comprimento: .2f}')
comprimento = comprimento * 0.08
print(f'EM PÉS: { comprimento: .2f}')