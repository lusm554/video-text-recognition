from PIL import Image
import pytesseract
import cv2
import numpy as np

def read_image(img_filepath):
  return cv2.imread(img_filepath)

def preproc(image):
  # Конвертация изображения в оттенки серого
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  # Бинаризация изображения методом Otsu
  _, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
  # Удаление шума с использованием морфологических операций
  kernel = np.ones((1, 1), np.uint8)
  binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
  binary_image = cv2.medianBlur(binary_image, 3)
  return binary_image

def search_text(image):
  #image = Image.open(img_filepath)
  image = Image.fromarray(image)
  text = pytesseract.image_to_string(image, lang='rus')
  return text

def image_to_text(img_filepath):
  image = read_image(img_filepath)
  image = preproc(image)
  txt = search_text(image)
  return txt

if __name__ == '__main__':
  import os
  for root, dirs, files in os.walk('87_43_b11df3f344d0af773aac81e410ee_fhd'):
    for file in files:
      filepath = os.path.join(root, file)
      print(f'{filepath=}')
      txt = image_to_text(filepath)
      print(txt)

