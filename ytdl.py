from pytube import YouTube

# List of YouTube video URLs
video_urls = [
 
    # Add more video URLs here
]

# Function to download a video
def download_video(url, save_path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()  # Change to your preferred stream
        print(f"Downloading: {yt.title}")
        video.download(output_path = save_path)
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

# Specify the directory to save the videos
save_directory = './My Files/Downloads'

for url in video_urls:
    download_video(url, save_directory)
