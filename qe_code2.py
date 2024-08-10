import qrcode 

from PIL import Image 


qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=6 ,)


qr.add_data("https://kunalpal97.github.io/My-Portfolio/")

qr.make(fit=True)

img = qr.make_image(fill_color="black",back_color="white")


img.save("qr_img.png")