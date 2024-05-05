from pytube import YouTube
import os
import ssl

# Ignore SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context


# Function to download YouTube video
def download_video(video_url, output_path):
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(output_path)

# Example usage
video_url = "https://www.youtube.com/watch?v=0Wmgde5TySY"
output_path = '/Users/rzhang/ai_stock_analyzer/frames'

download_video(video_url, output_path)