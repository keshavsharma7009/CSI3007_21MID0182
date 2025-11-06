# First install ( pip install qrcode ) in the terminal

import qrcode
data = "https://www.google.com"
qr = qrcode.make(data)
qr.save("google_qr.png")
print("QR Code Has Been Generated")