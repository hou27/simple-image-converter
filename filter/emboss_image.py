from PIL import Image
from PIL import ImageFilter

def emboss(input_image, save_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.EMBOSS)
    filtered_image.save(save_image)

if __name__ == '__main__':
    emboss("./images/butterfly.jpg", "./images/butterfly_emboss.jpg")