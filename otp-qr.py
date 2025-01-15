#pip install opencv-python

import cv2

# Load the QR code image
image = cv2.imread("otp-qr-code.png")

# Initialize QR Code detector
detector = cv2.QRCodeDetector()

# Detect and decode the QR code
data, _, _ = detector.detectAndDecode(image)

if data:
    print(f"Decoded Data: {data}")
else:
    print("No QR code detected.")
