def video_links_reader(filepath, isheader=True):
  import csv
  with open(filepath, 'r') as csvfile:
    reader = csv.reader(csvfile)
    if isheader:
      headers = next(reader)
    for line in reader:
      if isheader:
        row = dict(zip(headers, line))
      else:
        row = line
      yield row

def download_video(src_url, dest_filepath):
  import urllib.request
  urllib.request.urlretrieve(src_url, dest_filepath)

def download_first_100_videos(src_filepath, dest_dir):
  import sys, os
  print(f'{src_filepath=}')
  print(f'{dest_dir=}')
  links_reader = video_links_reader(src_filepath)
  for n, row in enumerate(links_reader):
    if n == 100:
      break
    video_url_src = row['link']
    _video_file = video_url_src.replace('https://cdn-st.rutubelist.ru/media', '').replace('/', '_').strip('_')
    video_filepath_dest = os.path.join(dest_dir, _video_file)
    print(f'{video_url_src=}')
    print(f'{video_filepath_dest=}')
    if os.path.exists(video_filepath_dest):
      print(f'File exists {video_filepath_dest}')
      continue
    download_video(video_url_src, video_filepath_dest)

def download_first_100_videos_cli():
  import sys, os
  try:
    src_filepath = sys.argv[1]
    dest_dir = sys.argv[2]
  except:
    src_filepath = 'yappy_hackaton_2024_400k.csv'
  download_first_100_videos(src_filepath, dest_dir)

if __name__ == '__main__':
  download_first_100_videos_cli()

