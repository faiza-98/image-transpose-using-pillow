from PIL import Image

# Relative Path
img = Image.open("picture.png")

# transposing image
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

# Save transposed image
transposed_img.save("transposed.jpg")
transposed_img.show()
