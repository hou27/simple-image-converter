from PIL import Image

def grayscale(original_image, new_image):
    color_image = Image.open(original_image)
    grayscale_image = color_image.convert("L") # convert to grayscale
    grayscale_image.save(new_image)