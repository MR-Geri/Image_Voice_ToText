from typing import Union
import cv2
import pytesseract


config = r'--oem 3 --psm 6'


def image_to_text(path: str) -> Union[None, str]:
    try:
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return pytesseract.image_to_string(img, config=config, lang='rus')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    pass
