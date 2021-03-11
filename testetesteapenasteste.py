alo = int(input('1 para converter cm pra polegadas \n2 para converter polegadas pra cm \n'))
print(alo)

if(alo == 1):
    cm = float(input('Indique quantos cm são: '))
    print('{} centimetros da {:.2f} polegadas'.format(cm, (cm / 2.54)))

elif(alo == 2):
    polegada1 = float(input('Indique quantas polegadas são: '))
    print('{} polegadas são {} cm'.format(polegada1, (polegada1 * 2.54)))
