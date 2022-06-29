termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
y = 1
n = termo + (10)*razão
while y != 0:
    while termo != n:
        print(termo, end = ' → ')
        termo += razão
    print('Pausa ')
    y = int(input('Mais quantos termos você deseja ver?: '))
    n = termo + y*razão
print('Fim!')