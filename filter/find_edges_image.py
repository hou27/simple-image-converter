from PIL import Image
from PIL import ImageFilter

def find_edges(input_image, save_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.FIND_EDGES)
    filtered_image.save(save_image)

if __name__ == '__main__':
    find_edges("./images/butterfly.jpg", "./images/butterfly_find_edges.jpg")