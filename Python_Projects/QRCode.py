import pyqrcode

url = "https://www.youtube.com/@Update_yourself1"

k=pyqrcode.create(url)
k.svg("Qr.svg", scale=10)