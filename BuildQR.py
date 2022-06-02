import qrcode
from PIL import Image

#===============================================================================
# Simple generation of QrCode

#generate_image = qrcode.make("https://www.youtube.com/watch?v=iik25wqIuFo")
#generate_image.save('image1.png')

#===============================================================================

# Utilizing the class QRcode 
qr = qrcode.QRCode(
    version = 1,                                              # size of qrCode, can be 1 to 40
    error_correction = qrcode.constants.ERROR_CORRECT_H,      # corrects disfigurations in image. Code H- 30% of errrors can be corrected
    box_size = 10,                                            # number of pixels per box in Qr Code
    border = 5,                                               # thickness of the border around boxes. default 4- min.size
)

qr.add_data('https://www.youtube.com/watch?v=iik25wqIuFo')    # =)
qr.make(fit = True)

img = qr.make_image(fillColor = 'black', 
                   backColor='white').convert('RGB')          # make qr code black and white


# Utilizing pillow library to add an overlay image to QR code just for fun '

imageDisplay = Image.open('rose.png')
imageDisplay.thumbnail((100,100))

# The following will calculate the center position and overlay the thumbnail image on top of the 
# QR code with the paste function

imagePos = ((img.size[0]-imageDisplay.size[0]) // 2, (img.size[1] - imageDisplay.size[1]) // 2)

img.paste(imageDisplay, imagePos)

img.save("sample2.png")