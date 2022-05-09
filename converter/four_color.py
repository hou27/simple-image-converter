from PIL import Image

def four_color(original_image, new_image):
    color_image = Image.open(original_image)
    four_color_image = color_image.convert("P", palette=Image.Palette.ADAPTIVE, colors=4) # convert to four color
    four_color_image.save(new_image)


