#!/usr/bin/env python
import yt_dlp

def download_video(url, output_path="."):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: ./downloader-yt <nombre>")
        sys.exit(1)
    url = sys.argv[1]
    download_video(url)
