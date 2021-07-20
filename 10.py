money = float(input('Quantos reais voce tem R$?'))
print('Com R${:.2f} voce consegue comprar:\n'
      '{:.2f} Dolares!\n'
      '{:.2f} Euros!\n'
      '{:.2f} Pesos!'.format(money, (money / 5.33), (money/6.42), (money/0.60)))