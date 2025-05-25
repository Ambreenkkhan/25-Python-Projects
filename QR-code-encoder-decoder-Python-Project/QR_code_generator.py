import qrcode

# Data to encode
data = "Sir Zian Khan"

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qrcode.png")

print("QR code generated and saved as my_qrcode.png")
