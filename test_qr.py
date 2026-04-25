from pip import qrcode
import os

print("Script started")

qr = qrcode.QRCode(version=1, box_size=10, border=5)
print("QR Code object created")

qr.add_data('https://example.com')
print("Data added to QR code")

qr.make(fit=True)
print("QR code generated")

img = qr.make_image(fill_color="black", back_color="white")
print("Image created")

save_path = os.path.join(os.path.dirname(__file__), 'test_qr.png')
img.save(save_path)
print(f"Image saved to: {save_path}")

print("Script completed")