preço = float(input('Qual o valor do produto?'))
porcentagem = float(input('Qual o valor do desconto?'))
desconto = (preço * porcentagem) / 100
newprice = preço - desconto

print('O preço original é R${:.2f}\n'
      'o valor do desconto é de R${:.2f}\n'
      'o valor final do produto é de R${:.2f}.'
      .format(preço, desconto, newprice))