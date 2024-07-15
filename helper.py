import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import PIL.Image
import time
from markdown import Markdown
import streamlit as st

load_dotenv()


GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY


def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))




def llm_model_audio(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.5-pro')
    prompt1="""
    You are a helpful assistant named 'ShauryaNova' developed by Ayush Shaurya Jha. You are
    supposed to answer accurately and precisely to the user's 
    question.Now, the user query begins :
    """
    content = f"{prompt1}\n{user_text}"
    response = model.generate_content(content)
    result = response.text
    result_cleaned = result.replace('*', '')
    return result_cleaned




def llm_model_image(user_text,path):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.5-pro')
    prompt1="""
    You are a helpful assistant named 'ShauryaNova' developed by  Ayush Shaurya Jha. You are
    supposed to answer accurately and precisely to the user's 
    question and image .Now, the user query begins :
    """
    sample_file = PIL.Image.open(path)
    prompt = f"{prompt1}\n{user_text}"
    response = model.generate_content([prompt, sample_file])
    result = response.text
    
    return result




def llm_model_video(user_text, video_path):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.5-pro')
    
    prompt1 = """
    You are a helpful assistant named 'ShauryaNova' developed by  Ayush Shaurya Jha .You are
    supposed to answer accurately and precisely to the user's 
    question and video. Now, the user query begins:
    """
    
    if video_path:
        video_file_name = video_path
    else:
        raise ValueError("Video path cannot be None")

    st.write(f"Uploading file: {video_file_name}")
    video_file = genai.upload_file(path=video_file_name)
    st.write(f"Completed upload: {video_file.uri}")

    # Check whether the file is ready to be used.
    while video_file.state.name == "PROCESSING":
        st.write('.', end='')
        time.sleep(10)
        video_file = genai.get_file(video_file.name)

    if video_file.state.name == "FAILED":
        raise ValueError(video_file.state.name)

    prompt = f"{prompt1}\n{user_text}" if user_text else prompt1
    response = model.generate_content([video_file,prompt] ,request_options={"timeout": 600})
    result = response.text

    return result

    
    
def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("speech.mp3")





