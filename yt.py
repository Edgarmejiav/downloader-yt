from pytube import YouTube
def download_video(url, output_path='./'):
    try:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        video_info = {
            "title": video.title,
            "author": video.author,
            "filename": stream.default_filename,
            "destination_path": output_path
        }
        stream.download(output_path=output_path)
        return video_info
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    download_video(url="https://youtu.be/3AtDnEC4zak?list=RD8PTDv_szmL0")
