from util import helpers
import uuid
import os


def generate_videos(videos):
    for type in videos:
        response = helpers.generate_story(type)
        helpers.generate_speech(response.text)
        helpers.generate_srt()
        helpers.generate_video(f'output/{type.value.replace(' ', '_')}_{uuid.uuid1()}')            
        os.remove('audio.mp3')
        os.remove('subtitles.srt')
