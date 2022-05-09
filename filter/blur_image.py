from PIL import Image
from PIL import ImageFilter

def blur(input_image, save_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.BLUR)
    filtered_image.save(save_image)

if __name__ == '__main__':
    blur("./images/butterfly.jpg", "./images/butterfly_blur.jpg")