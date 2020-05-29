import urllib.request
from PIL import Image
#Save the image from the imgur.com url provided
image = Image.open(urllib.request.urlopen('https://i.imgur.com/BDTnVgy.jpg'))
# Create 3 new images that are resized copies of the original image and save them
A = image.resize((100, 100)) #A is resized to 100x100
A.save('A.jpg')
B = image.resize((500, 500)) #B is resized to 500x500
B.save('B.jpg')
C = image.resize((1024, 1024)) #C is resized to 1024x1024
C.save('C.jpg')

