valor= float(input('Digite valor da metragem para ser convertido:  '))

quilometro= valor / 1000

hectometro= valor / 100

decametro= valor / 10

decimetros= valor * 10

centimetros= valor * 100

milimetros= valor * 1000

print(f'Valor informado é {valor}m;\n'
      f' convertido em Quilômetro {quilometro}km;\n'
      f' convertido em Hectômetro {hectometro}hm;\n'
      f' convertido em Decâmetro {decametro}dam;\n'
      f' convertido em Decímetro {decimetros}dm;\n'
      f' convertido em centímetro é {centimetros}cm;\n'
      f' convertido em milímetro é {milimetros}mm.')
