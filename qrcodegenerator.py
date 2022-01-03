import qrcode
import image
qr = qrcode.QRCode(
    version = 20,
    box_size = 16,
    border = 8
)

data = "https://github.com/danish20000"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",black_color="white")
img.save("qrcode.png")