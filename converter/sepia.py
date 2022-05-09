from PIL import Image

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