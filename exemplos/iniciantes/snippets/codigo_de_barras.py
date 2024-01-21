
#python-barcode

import barcode
from barcode.writer import ImageWriter

# Gerar um código de barras EAN13
ean = barcode.get('ean13', '123456789012', writer=ImageWriter())
filename = ean.save('codigo_de_barras')

# O arquivo 'codigo_de_barras.png' será salvo com o código de barras
