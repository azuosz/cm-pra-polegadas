alo = int(input('Escolha 1 para converter cm pra polegadas ou 2 para converter polegadas pra cm '))
print(alo)

if(alo == 1):
    cm = float(input('Indique quantos cm são: '))
    polegada = cm / 2.54
    print('{} centimetros da {} polegadas'.format(cm, polegada))

elif(alo == 2):
    polegada1 = float(input('Indique quantas polegadas são: '))
    cm1 = polegada1 * 2.54
    print('{} polegadas são {} cm'.format(polegada1, cm1))
