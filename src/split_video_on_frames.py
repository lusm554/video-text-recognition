import cv2
import numpy as np
from pathlib import Path

def video_to_frames(video_filepath, frames_dest_dir, num_frames=10):
  print(f'{video_filepath=}')
  print(f'{frames_dest_dir=}')
  print(f'{num_frames=}')
  video = cv2.VideoCapture(video_filepath)
  if not video.isOpened():
    raise Error('Could not open video')
  fps = video.get(cv2.CAP_PROP_FPS)
  frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
  print(f'{fps=}')
  print(f'{frame_count=}')
  # Создает массив из num_frames чисел, равномерно распределенных в диапазоне от 0 до frame_count-1.
  frame_idx = np.linspace(0, frame_count-1, num=num_frames, dtype=int)
  '''
  Эта строка помогает равномерно распределить кадры по всей длине видео, чтобы получить репрезентативные кадры,
  отражающие содержание всего видео.
  Таким образом, вместо извлечения подряд идущих кадров в начале или конце видео,
  получаются кадры из всех частей видео, что даёт более полное представление о его содержании.
  '''
  frames_dest_path_obj = Path(frames_dest_dir)
  frames_dest_path_obj.mkdir(exist_ok=True) # create dir for frames if not exist
  for frame_offset in frame_idx:
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_offset)
    ret, frame = video.read()
    if ret:
      frame_filepath = str(frames_dest_path_obj.joinpath(f'frame_{frame_offset}.jpg'))
      print(frame_filepath)
      cv2.imwrite(frame_filepath, frame)
  video.release() 
  cv2.destroyAllWindows()

if __name__ == '__main__':
  #video_filepath = 'videos/87_43_b11df3f344d0af773aac81e410ee_fhd.mp4'
  import sys
  video_filepath = sys.argv[1]
  frames_dest_base_path = video_filepath.split('/')[-1].replace('.mp4', '')
  video_to_frames(video_filepath, frames_dest_base_path)


