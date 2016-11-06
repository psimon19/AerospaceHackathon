from PIL import Image 

filename = "trackingImage.png"
image = Image.open("trackingImage.png")
grayscale = image.convert('L')
minima, maxima = grayscale.getextrema()
maxPointX = 0
maxPointY = 0


for width in range(0, image.size[0]):
   for height in range(0, image.size[1]):
       if grayscale.getpixel((width, height)) == maxima:
       		maxPointX = width
       		maxPointY = height

print "Value is at: (%d, %d)", maxPointX, maxPointY 