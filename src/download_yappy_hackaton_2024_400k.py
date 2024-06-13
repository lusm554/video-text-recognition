def download_video(src_url, dest_filepath):
  import urllib.request
  urllib.request.urlretrieve(src_url, dest_filepath)


download_video('https://downloader.disk.yandex.ru/disk/34eb54c75c24ecd29d7e160e2981ef56185a4d1016719295c5aa15daadd557d1/6664d733/C-qvzXhq3Qv4Jn8bQZpgY3zSlcRCuHA1hUz_zQoJniIVawbEPmiT0p1kHEbAYVfGOHmHvIiAf9UGKKtZm99E7Q%3D%3D?uid=0&filename=yappy_hackaton_2024_400k.csv&disposition=attachment&hash=O2xRCRHTmIL1vxRM4Un/2bC82ztax4AIABrbegDU4iauwxJf2U37PBpUQ8UlOI0hq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=text%2Fplain&owner_uid=533823195&fsize=68176276&hid=cb583d0003ab9b41328bc7f4fe68e11b&media_type=spreadsheet&tknv=v2', 'yappy_hackaton_2024_400k.csv')
