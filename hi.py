import qrcode
import os

def generate_qr_code(data, filename):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the data
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    save_path = os.path.join(os.path.dirname(__file__), filename)
    img.save(save_path)
    print(f"QR Code saved as {save_path}")

# Usage
data = "https://www.example.com"
filename = "example_qr.png"
generate_qr_code(data, filename)