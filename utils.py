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
def check_text_equality(text1,text2):
    if text1 == text2:
        return True
    else:
        raise TextIsDifferent('The text on the page is different than expected')