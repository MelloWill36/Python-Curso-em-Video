larg = float(input('Qual a largura da parede?'))
altura = float(input('Qual a altura da parede?'))
area = larg * altura
tinta = (area / 2)

print('As dimensões da sua parede saõ {:.2f}m de largura e tem {:.2f}m de altura.\n'
      'A area é de {:.2f}m2 e você vai precisar de {:.2f} litros de tinta para pintar a parede toda!'
      .format(larg, altura, area, tinta))