import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)  # here we give our QrCode sige 

qr.add_data("https://www.youtube.com/")  #here, we give link which site we want to create QrCode
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white") #here we give color effect of our qr code Background or front
img.save("Youtube.png")  #here we define saving of image i.e., in jpg or png form


#Made by Anuj Yadav