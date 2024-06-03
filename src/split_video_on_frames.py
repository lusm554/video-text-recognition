import cv2
import numpy as np

def get_frames(path_to_video, num_frames=10):
  video = cv2.VideoCapture(path_to_video)
  if not video.isOpened():
    raise Error('Could not open video')
  fps = video.get(cv2.CAP_PROP_FPS)
  frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
  print(f'{fps=}')
  print(f'{frame_count=}')
  frame_idx = np.linspace(0, frame_count-1, num=num_frames, dtype=int)
  for frame_offset in frame_idx:
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_offset)
    ret, frame = video.read()
    if ret:
      frame_filepath = f'test_{frame_offset}.jpg'
      cv2.imwrite(frame_filepath, frame)
  video.release() 
  cv2.destroyAllWindows()

get_frames('videos/87_43_b11df3f344d0af773aac81e410ee_fhd.mp4')

