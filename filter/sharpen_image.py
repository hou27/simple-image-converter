from PIL import Image
from PIL import ImageFilter

def sharpen(input_image, save_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.SHARPEN)
    filtered_image.save(save_image)

if __name__ == '__main__':
    sharpen("./images/butterfly.jpg", "./images/butterfly_sharpen.jpg")