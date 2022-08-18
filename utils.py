import io
from PIL import Image, ImageChops


def is_images_equal(img1, img2):
    image_1 = Image.open(io.BytesIO(img1)).convert('RGB')
    image_2 = Image.open(io.BytesIO(img2)).convert('RGB')
    result = ImageChops.difference(image_1, image_2).getbbox()
    if result is None:
        return True
    return False