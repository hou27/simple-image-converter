from PIL import Image
from PIL import ImageFilter

def contour(input_image, save_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.CONTOUR)
    filtered_image.save(save_image)

if __name__ == '__main__':
    contour("./images/butterfly.jpg", "./images/butterfly_contour.jpg")