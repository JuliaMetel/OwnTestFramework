import io
from PIL import Image, ImageChops
from exception import TextIsDifferent


def is_images_equal(img1, img2):
    image_1 = Image.open(io.BytesIO(img1)).convert('RGB')
    image_2 = Image.open(io.BytesIO(img2)).convert('RGB')
    result = ImageChops.difference(image_1, image_2).getbbox()
    if result is None:
        return True
    return False


def is_text_equal(text1, text2):
    return text1 == text2


def check_text_equal(text1, text2):
    if not (is_text_equal(text1, text2)):
        raise TextIsDifferent('The text on the page is different than expected')


def check_text_not_equal(text1, text2):
    if is_text_equal(text1, text2):
        raise TextIsDifferent('The text on the page is as expected')
