from PIL import Image, ImageFilter

img = Image.open('./assets/astro.jpg')

# print(img.format)
# print(img.size)
# print(img.mode)
#
# print(dir(img))


# filtered_img = img.filter(ImageFilter.BLUR)
#
# filtered_img.save("blur.png", "png")

# filtered_img = img.filter(ImageFilter.SMOOTH)
#
# filtered_img.save("smooth.png", "png")
#
# filtered_img = img.filter(ImageFilter.SHARPEN)
#
# filtered_img.save("sharpen.png", "png")


# filtered_img = img.convert('L')  # Converts to grayscale

# filtered_img = img
# resize = filtered_img.resize((100, 100))
# resize.save("resize.png", "png")
# filtered_img.show()

# filtered_img = img
# box = (100, 100, 400, 400)  # (left, upper, right, lower)
# region = filtered_img.crop(box)
# region.save("crop.png", "png")

img.thumbnail((400, 400))  # Keeps aspect ratio of original photo, will do anything within width/height of tuple values

img.save("astro_new.png", "png")