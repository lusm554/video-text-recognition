import cv2
import numpy as np
import os

def video_to_frames(video_filepath, frames_dest_base_path, num_frames=10):
  print(f'{video_filepath=}')
  print(f'{frames_dest_base_path=}')
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
  for frame_offset in frame_idx:
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_offset)
    ret, frame = video.read()
    if ret:
      frame_filepath = os.path.join(frames_dest_base_path, f'frame_{frame_offset}.jpg')
      print(frame_filepath)
      #cv2.imwrite(frame_filepath, frame)
  video.release() 
  cv2.destroyAllWindows()

if __name__ == '__main__':
  video_filepath = 'videos/87_43_b11df3f344d0af773aac81e410ee_fhd.mp4'
  frames_dest_base_path = video_filepath.split('/')[-1].replace('.mp4', '')
  video_to_frames(video_filepath, frames_dest_base_path)


