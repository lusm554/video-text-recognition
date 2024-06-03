import cv2

def get_frames(path_to_video):
  video = cv2.VideoCapture(path_to_video)
  if not video.isOpened():
    raise Error('Could not open video')
  fps = video.get(cv2.CAP_PROP_FPS)
  frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
  print(f'{fps=}')
  print(f'{frame_count=}')
  frame_num = 0
  while video.isOpened():
    ret, frame = video.read()
    if not ret:
      break
    if frame_num % 10 == 0:
      frame_filepath = f'test_{frame_num}.jpg'
      cv2.imwrite(frame_filepath, frame)
    frame_num += 1
  video.release() 

get_frames('videos/87_43_b11df3f344d0af773aac81e410ee_fhd.mp4')

