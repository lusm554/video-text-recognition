from setup_environment import (
  download_yappy_hackaton_2024_400k,
  download_easyocr_model,
  download_first_100_videos,
)
from pathlib import Path

def for_test_download():
	yappy_hackaton_2024_400k_dest_filepath='yappy_hackaton_2024_400k.csv'
	videos_download_dir = 'videos'
	Path(videos_download_dir).mkdir(parents=True, exist_ok=True)
	#download_yappy_hackaton_2024_400k(dest_filepath=yappy_hackaton_2024_400k_dest_filepath)
	download_first_100_videos(src_filepath=yappy_hackaton_2024_400k_dest_filepath, dest_dir=videos_download_dir)

def main_download():
	download_easyocr_model()

if __name__ == '__main__':
	import sys
	try:
		download_type = sys.argv[1]
	except:
		download_type = None
	main_download()
	if download_type == 'test':
		for_test_download()
