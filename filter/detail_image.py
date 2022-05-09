from PIL import Image
from PIL import ImageFilter

def detail(input_image, save_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.DETAIL)
    filtered_image.save(save_image)

if __name__ == '__main__':
    detail("./images/butterfly.jpg", "./images/butterfly_detail.jpg")