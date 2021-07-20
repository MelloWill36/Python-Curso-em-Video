medida = float(input('Digite uma medida em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
km = medida / 1000
x = medida / 100
y = medida / 10

print('Sua medida em DM é: {:.2f}; \n Sua medida em CM é: {:.2f}; \n Sua medida em MM é: {:.2f}; '
      '\n Sua medida em KM é: {:.2f}; \n Sua medida em X é: {:.2f}; \n Sua medida em Y é: {:.2f}; \n'
      .format(dm, cm, mm, km, x, y))
