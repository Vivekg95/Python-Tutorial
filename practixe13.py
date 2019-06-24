import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('C:\\Users\\Vivek Kumar\\Desktop\\python10\\Some data.png')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")