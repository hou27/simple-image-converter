from PIL import Image

def grayscale(original_image, new_image):
    color_image = Image.open(original_image)
    grayscale_image = color_image.convert("L") # convert to grayscale
    grayscale_image.save(new_image)

def bw(original_image, new_image):
    color_image = Image.open(original_image)
    bw_image = color_image.convert("1") # convert to black and white
    bw_image.save(new_image)

def bw_dithering(original_image, new_image):
    color_image = Image.open(original_image)
    bw_image = color_image.convert("1", dither=0) # convert to black and white
    bw_image.save(new_image)

def four_color(original_image, new_image):
    color_image = Image.open(original_image)
    four_color_image = color_image.convert("P", palette=Image.Palette.ADAPTIVE, colors=4) # convert to four color
    four_color_image.save(new_image)

def make_sepia_palette(base_color):
    palette = []
    r, g, b = base_color
    for i in range(255):
        new_red = r * i // 255
        new_green = g * i // 255
        new_blue = b * i // 255
        palette.extend( (new_red, new_green, new_blue) )
    return palette

def create_sepia(original_image, new_image):
    whitish = (255, 240, 192)
    sepia = make_sepia_palette(whitish)
    color_image = Image.open(original_image)

    gray_scale = color_image.convert("L") # convert to grayscale
    gray_scale.putpalette(sepia) # set sepia palette

    sepia_image = gray_scale.convert("RGB")
    sepia_image.save(new_image)
