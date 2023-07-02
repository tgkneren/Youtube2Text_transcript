from youtube_transcript_api import YouTubeTranscriptApi


def download_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = ""
    for segment in transcript:
        text += segment['text'] + ' '
    return text


def save_text_to_file(text, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print("Text file saved")
    except Exception as e:
        print("An error occurred while saving the text file:", str(e))


video_id = 'QXWNChoIluo'  # https://www.youtube.com/watch?v=QXWNChoIluo (youtube link id)
transcript_text = download_transcript(video_id)
save_text_to_file(transcript_text, 'transcript.txt')
