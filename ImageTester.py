from PIL import Image, ImageDraw

fileName = "StressTest.jpg"
image = Image.open(fileName)
grayscale = image.convert('L')
#minima, maxima = grayscale.getextrema()
maxima = 0
maxPointX = 0
maxPointY = 0


for width in range(0, image.size[0]):
   for height in range(0, image.size[1]):
       if grayscale.getpixel((width, height)) > maxima:
       		maxima = grayscale.getpixel((width, height))
       		maxPointX = width
       		maxPointY = height

#image = Image.open(fileName)
draw = ImageDraw.Draw(image)
draw.rectangle(((maxPointX - 15, maxPointY-15),(maxPointX + 15, maxPointY + 15)), fill=None, outline = "red")
del draw
image.save("imageout3.png")
print "Value is at: (%d, %d)", maxPointX, maxPointY 