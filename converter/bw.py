from PIL import Image

def bw(original_image, new_image):
    color_image = Image.open(original_image)
    bw_image = color_image.convert("1") # convert to black and white
    bw_image.save(new_image)

def bw_dithering(original_image, new_image):
    color_image = Image.open(original_image)
    bw_image = color_image.convert("1", dither=0) # convert to black and white
    bw_image.save(new_image)