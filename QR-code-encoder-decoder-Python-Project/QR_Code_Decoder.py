from pyzbar.pyzbar import decode
from PIL import Image

# Load the image
img = Image.open("my_qrcode.png")

# Decode the QR code
decoded_objects = decode(img)

# Print the decoded data
for obj in decoded_objects:
    print("Decoded Data:", obj.data.decode("utf-8"))

print("QR code decoded successfully")