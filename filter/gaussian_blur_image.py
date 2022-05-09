from PIL import Image
from PIL import ImageFilter

def gaussian_blur(input_image, save_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.GaussianBlur(radius=5))
    filtered_image.save(save_image)

if __name__ == '__main__':
    gaussian_blur("./images/butterfly.jpg", "./images/butterfly_gaussian_blur.jpg")