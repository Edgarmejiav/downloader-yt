#!/usr/bin/env python
from pytube import YouTube

def download_video(url, output_path='./'):
    print("1")
    try:
        video = YouTube(url)
        print("2")
        stream = video.streams.get_highest_resolution()
        video_info = {
            "title": video.title,
            "author": video.author,
            "filename": stream.default_filename,
            "destination_path": output_path
        }
        print("3")
        stream.download(output_path=output_path)
        print("Video descargado con éxito!" + video_info["filename"])
        return video_info
    except Exception as e:
        return {"error": str(e)}

def say_hello(name):
    print(f"Hola {name}!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: ./downloader-yt <nombre>")
        sys.exit(1)
    name = sys.argv[1]
    say_hello(name)
    # download_video(url="https://youtu.be/3AtDnEC4zak?list=RD8PTDv_szmL0")
