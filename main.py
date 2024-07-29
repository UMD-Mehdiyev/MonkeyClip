from init import generate_videos
from util import content


"""
Content Options:
* Shower Thought
* Funny Story
* Horror Story
* Biography
* Mystery Story
* Romantic Story
* Mythology Story
* Fantasy Story
* Historical Story
* Fable
"""    
videos = [
    content.StoryType.HORROR_STORY,
    content.StoryType.SHOWER_THOUGHT,
    content.StoryType.ROMANTIC_STORY,
    content.StoryType.FUNNY_STORY,
    content.StoryType.FABLE
]

if __name__ == "__main__":
    generate_videos(videos)