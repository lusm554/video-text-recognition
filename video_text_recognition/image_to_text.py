import easyocr
from PIL import Image
import cv2

def read_image_from_file(img_filepath):
  return cv2.imread(img_filepath)

def resize_image(img):
  n_width=720
  n_height=1280
  return cv2.resize(img, (n_width, n_height))

def get_reader(reader_cfg):
  # docs - https://www.jaided.ai/easyocr/documentation/
  reader_default_cfg = {
    'lang_list': ['ru', 'en'],
    'gpu': True,
    'download_enabled': False,
    'model_storage_directory': './EasyOCR/model/',
  }
  reader_cfg = {**reader_default_cfg, **reader_cfg}
  reader = easyocr.Reader(**reader_cfg)
  return reader

def list_images_to_text(images, reader=None, reader_cfg={}):
  images = [
    resize_image(read_image_from_file(image)) if isinstance(image, str) else image
    for image in images
  ]
  if reader is None:
    reader = get_reader(reader_cfg)
  results = reader.readtext_batched(
    images,
  )
  result = [
    ' '.join(r[1] for r in img_result)
    for img_result in results
  ]
  return result

def image_to_text(image, reader=None, reader_cfg={}):
  if isinstance(image, str): # check if image path is str/filepath
    image = read_image_from_file(image)
  if reader is None:
    reader = get_reader(reader_cfg)
  results = reader.readtext(image=image)
  result_text = ' '.join(r[1] for r in results)
  return result_text

if __name__ == '__main__':
  import sys
  from pprint import pprint
  # Single image
  '''
  img_filepath = sys.argv[1]
  print(f'{img_filepath=}')
  img_text = image_to_text(img_filepath)
  print(img_text)
  '''
  # Multiple images
  img_dir_filepath = sys.argv[1]
  print(f'{img_dir_filepath=}')
  import glob
  img_files = glob.glob(f'{img_dir_filepath}/*')
  img_text = list_images_to_text(img_files)
  pprint(dict(zip(img_files, img_text)))

