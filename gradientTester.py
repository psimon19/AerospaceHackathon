from PIL import Image
filename = "trackingImage.png"

image = Image.open(filename)
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

print "Value is at: (%d, %d)", maxPointX, maxPointY 