def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("speech.mp3")

# gTTS--> Google text to speech
