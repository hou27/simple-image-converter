from PIL import Image
from PIL import ImageFilter

def smooth(input_image, save_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.SMOOTH)
    filtered_image.save(save_image)

if __name__ == '__main__':
    smooth("./images/butterfly.jpg", "./images/butterfly_smooth.jpg")