from PIL import Image, ImageDraw
fileName = "StressTest.png"

image = Image.open(fileName)
grayscale = image.convert("L")

maxPointX = 0
maxPointY = 0
maxChange = 0

pixel = 0
prevPx = 0

for width in range(0, image.size[0]):
	for height in range(0, image.size[1]):
		pixel = grayscale.getpixel((width, height))
   		if (maxChange < abs(pixel - prevPx)):
   			maxChange = abs(pixel - prevPx)
   			maxPointX = width
   			maxPointY = height
		prevPx = pixel;

image = Image.open(fileName)
draw = ImageDraw.Draw(image)
draw.rectangle(((maxPointX - 5, maxPointY-5),(maxPointX + 5, maxPointY + 5)), fill=None, outline = "red")
del draw
image.save("imageout2.jpg")

print "Value is at: (%d, %d)", maxPointX, maxPointY