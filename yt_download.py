import yt_dlp

def download_youtube_video(url):
    # Configure options for yt-dlp
    ydl_opts = {
        # Format string to download the best MP4 video and audio available
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s', # Save file with the video title
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Downloading: {url}")
            ydl.download([url])
            print("Download completed successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)