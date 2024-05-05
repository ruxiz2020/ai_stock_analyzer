from youtube_transcript_api import YouTubeTranscriptApi
import datetime

video_id = "8cXMQDI3K7E"
#transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
trans = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh'])

today = datetime.datetime.today().strftime('%Y-%m-%d')
with open(video_id + "_" + today + ".txt", "a") as file:
    for t in trans:
        file.write(t['text'])
        file.write("\n")
