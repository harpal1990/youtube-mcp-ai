from youtube_transcript_api import YouTubeTranscriptApi
from utils.youtube import extract_video_id

def get_transcript(url: str) -> str:
    video_id = extract_video_id(url)

    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id)

    return " ".join([t.text for t in transcript])