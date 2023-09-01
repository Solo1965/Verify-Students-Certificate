import qrcode

# URL to the HTML page you created
url = "https://github.com/Solo1965/Verify-Students-Certificate/commit/72211ca58ee8d8a22a2d7a66433beed26c4d4f90"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("certificate_verification_qr.png")
