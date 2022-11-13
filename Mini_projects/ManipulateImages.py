from PIL import Image

# Open the image
im = Image.open("image.jpg")

# Rotate the image 90 degrees clockwise
im.rotate(90).show()

# Rotate the image 180 degrees
im.rotate(180).show()


# Rotate the image 270 degrees
im.rotate(270).show()

# Flip the image left to right
im.transpose(Image.FLIP_LEFT_RIGHT).show()

# Flip the image top to bottom
im.transpose(Image.FLIP_TOP_BOTTOM).show()


