from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings
from util import gemini, content
from moviepy.editor import *
import assemblyai as aai
from gtts import gTTS
import random
import os


def generate_story(type: content.StoryType):
    model = gemini.create_model()
    prefix = "Create a short (about 30s to 1m long if read out loud) and realistic "
    return model.generate_content(prefix + type.value, safety_settings={
                                            'HARM_CATEGORY_SEXUALLY_EXPLICIT':'block_none',
                                            'HARM_CATEGORY_HATE_SPEECH':'block_none',
                                            'HARM_CATEGORY_HARASSMENT':'block_none',
                                            'HARM_CATEGORY_DANGEROUS_CONTENT':'block_none'
                                            })

def generate_speech(content):
    tts = gTTS(text=content, lang='en', tld='co.uk')
    tts.save("audio.mp3")
    print("Audio successfully saved!")

def generate_srt():
    aai.settings.api_key = os.getenv("SRT_API_KEY")
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe("audio.mp3")

    srt = transcript.export_subtitles_srt()
    with open("subtitles.srt", "w") as f:
        f.write(srt)


def generate_video(filename):
    change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})
    def subtitle_generator(txt):
        return TextClip(
            txt, 
            font='Impact', 
            fontsize=50, 
            color='white', 
            stroke_color='black', 
            stroke_width=1, 
            size=(540, 1280), 
            method='caption'
        )

    video = VideoFileClip(os.path.join("backgrounds", random.choice([f for f in os.listdir("backgrounds") if f.endswith('.mp4')])))
    audio = AudioFileClip("audio.mp3")
    audio_duration = audio.duration + 0.15
    video = video.loop(duration=audio_duration)
    subtitles = SubtitlesClip("subtitles.srt", subtitle_generator)
    video_with_subtitles = CompositeVideoClip([video, subtitles.set_position(('center', 'bottom'))])
    video_with_subtitles = video_with_subtitles.set_audio(audio)
    video_with_subtitles.write_videofile(f"{filename}.mp4", fps=24)
