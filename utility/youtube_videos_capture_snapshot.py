from pytube import YouTube
import cv2
import ssl

# Ignore SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Function to download YouTube video and extract frames with a 5-second interval
def extract_frames_with_interval(video_url, output_path, interval):
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

    # Download the video
    stream.download(output_path, filename='video')

    # Capture frames from the downloaded video
    cap = cv2.VideoCapture(output_path + '/stock_video.mp4')

    frame_count = 0
    elapsed_time = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Increment elapsed time by the time difference between frames
        elapsed_time += 1 / cap.get(cv2.CAP_PROP_FPS)

        # If elapsed time exceeds the interval, capture the frame
        if elapsed_time >= interval:
            cv2.imwrite(f'{output_path}/frame_{frame_count}.jpg', frame)
            frame_count += 1
            elapsed_time = 0  # Reset elapsed time

    cap.release()


# Example usage
video_url = 'https://www.youtube.com/watch?v=0Wmgde5TySY'
output_path = '/Users/rzhang/ai_stock_analyzer/frames'
interval = 5  # Interval between frames in seconds

extract_frames_with_interval(video_url, output_path, interval)