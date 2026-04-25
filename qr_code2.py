# how to make qr code
# Importing library
import qrcode
 
# Data to be encoded
data = 'hello nazeem'
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('nazeem.png')