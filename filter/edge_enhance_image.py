from PIL import Image
from PIL import ImageFilter

def edge_enhance(input_image, save_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.EDGE_ENHANCE)
    filtered_image.save(save_image)

if __name__ == '__main__':
    edge_enhance("./images/butterfly.jpg", "./images/butterfly_edge_enhance.jpg")