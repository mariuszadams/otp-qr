### requires pillow & pyzbar - latter may not work

from PIL import Image
from pyzbar.pyzbar import decode
import urllib.parse

# Load the QR code image
image = Image.open("otp-qr-code.png")  # Replace with your QR code file path

# Decode the QR code
decoded_data = decode(image)

if decoded_data:
    for obj in decoded_data:
        qr_data = obj.data.decode("utf-8")
        print(f"Decoded QR Data: {qr_data}")
        
        # Extract the base secret
        if "otpauth://" in qr_data:
            parsed = urllib.parse.urlparse(qr_data)
            query_params = urllib.parse.parse_qs(parsed.query)
            base_secret = query_params.get("secret", [""])[0]
            print(f"Base Secret: {base_secret}")
else:
    print("No QR code found in the image.")
