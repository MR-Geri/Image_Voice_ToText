from typing import Union
import cv2
import pytesseract
import imutils


config = r'--oem 3 --psm 6'


def image_to_text(path: str) -> Union[None, str]:
    try:
        image = cv2.imread(path)
        image = imutils.resize(image, width=int(1.5 * len(image[0])))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        # Invert, Blur, and perform text extraction
        invert = 255 - cv2.GaussianBlur(thresh, (3, 3), 0)
        data = pytesseract.image_to_string(invert, lang='rus', config=config)
        return data
    except Exception as e:
        print(e)


if __name__ == '__main__':
    pass
