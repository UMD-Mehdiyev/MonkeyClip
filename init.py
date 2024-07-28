from util import gemini

def run():
    print("Initializing MonkeyClip...")
    model = gemini.create_model()
    response = model.generate_content("Write a story about an AI and magic")
    print(response.text)