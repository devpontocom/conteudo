#pip install qrcode

import qrcode

conteudo_do_qrcode = "https://www.devponto.com"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(conteudo_do_qrcode)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.show()