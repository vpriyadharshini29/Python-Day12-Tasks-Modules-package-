import qrcode

data = input("Enter data for QR: ")
img = qrcode.make(data)
img.save("myqr.png")
print("QR Code generated and saved as myqr.png")
