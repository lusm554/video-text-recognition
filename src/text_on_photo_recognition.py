from PIL import Image
import pytesseract

def img_to_text(img_filepath):
  image = Image.open(img_filepath)
  text = pytesseract.image_to_string(image, lang='rus')
  return text

filepath = '87_43_b11df3f344d0af773aac81e410ee_fhd/frame_646.jpg'
txt = img_to_text(filepath)
print(txt)

