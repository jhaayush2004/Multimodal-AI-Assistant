---
title: Multimodal AI Assistant
emoji: 🤖
colorFrom: blue
colorTo: teal
sdk: streamlit
sdk_version: 1.36.0
app_file: python main.py
pinned: false
---

# Multimodal AI Assistant

The Multilingual AI Assistant project leverages cutting-edge technologies to provide a versatile assistant capable of handling text, image, and video inputs. Powered by Google's `Gemini-1.5-pro` model and integrated with `gTTS` (Google Text-to-Speech), `PIL` (Python Imaging Library), and `SpeechRecognition`, this assistant offers a seamless user experience across multiple modalities.

## Why Google Gemini-1.5-pro ?
- At the heart of **Gemini 1.5 Pro's** advancements is its `1M token context window`. This feature allows the model to analyze and understand inputs of unparalleled length, enabling deeper and more nuanced content generation and data analysis.
- **Gemini 1.5 Pro** leverages the `Mixture of Experts (MoE)` architecture, enhancing its ability to process and respond to complex queries efficiently. This architecture allows the model to delegate tasks to specialized components, significantly boosting its performance and versatility.
- With its `vast context window` and advanced architecture, **Gemini 1.5 Pro** demonstrates `superior information retrieval capabilities`. This allows for more precise and relevant outputs, particularly in tasks requiring the extraction of specific information from large datasets.

![App Screenshot](https://github.com/jhaayush2004/Multimodal-AI-Assistant/blob/main/visuals/Gemini-Pro-1.5.png)

## Technologies and Tools Used:

`Google Gemini-1.5-pro` : Utilized for generating contextually relevant responses across various inputs such as text, images, and videos.

`gTTS (Google Text-to-Speech)` : Converts textual responses into natural-sounding speech for user interaction.

`PIL (Python Imaging Library)` : Handles image processing tasks, allowing the assistant to analyze and interpret visual content.

`SpeechRecognition` : Enables voice input recognition, enhancing user interaction through spoken commands.

`google-generativeai` : Provides tools for interacting with Google's generative AI services

`Streamlit` : Used for developing the interactive user interface (UI), making it easy to deploy and visualize outputs.

`Python(3.10.9)` : Primary programming language used for implementing the backend logic and integrating various components.

`Other libraries` : Includes standard Python libraries for file handling, audio manipulation, and API integrations.

![App Screenshot](https://github.com/jhaayush2004/Multimodal-AI-Assistant/blob/main/visuals/1M.jpg)

## Key features

`Multimodal Inputs` : Supports text queries, image uploads, and video submissions for generating informative responses.

`Voice Interaction` : Enables users to interact with the assistant using voice commands, which are processed using SpeechRecognition.

`Real-time Response Generation` : Utilizes Gemini-pro's capabilities to generate context-aware responses in real-time, enhancing user engagement and satisfaction.

`Speech Output` : Converts textual responses into audio format using gTTS, allowing users to listen to responses directly.


## Model Pipeline Overview

1. **Input Handling**
   - **Speech Recognition (SpeechRecognition):**
     - **Functionality:** Converts spoken language into text.
     - **Tool:** Utilizes various speech recognition engines and APIs.
     - **Implementation:** Integrated to capture user queries through voice input.
   
   - **Text Input:**
     - **Functionality:** Accepts textual queries directly from users.
     - **Implementation:** Utilizes Streamlit for creating interactive input fields.

   - **File Upload (Streamlit):**
     - **Functionality:** Allows users to upload images and videos.
     - **Implementation:** Streamlit's file uploader widget integrated for image and video input.

2. **Data Processing**
   - **Audio Processing (PyAudio):**
     - **Functionality:** Enables recording and processing of audio data.
     - **Tool:** Interfaces with the PortAudio library.
     - **Implementation:** Used for capturing and handling voice inputs.

   - **Image Processing (PIL - Python Imaging Library):**
     - **Functionality:** Performs operations on image data, such as opening, manipulating, and saving.
     - **Implementation:** Used to handle image uploads and processing before model input.

   - **Video Processing (Streamlit):**
     - **Functionality:** Handles video file uploads and processing.
     - **Implementation:** Streamlit utilized to manage video file uploads and subsequent actions.

3. **Model Integration**
   - **Google Generative AI Services (google-generativeai):**
     - **Functionality:** Accesses and interacts with Google's generative AI models.
     - **Tool:** Facilitates model integration for generating responses based on input queries.
     - **Implementation:** Used to generate content or responses based on user inputs, both text and multimodal.

4. **Output Generation**
   - **Text-to-Speech (gTTS - Google Text-to-Speech):**
     - **Functionality:** Converts generated text responses into spoken audio.
     - **Tool:** Utilizes Google's Text-to-Speech API.
     - **Implementation:** Generates audio output for user queries and responses.

5. **User Interface (Streamlit and Markdown)**
   - **Streamlit:**
     - **Functionality:** Framework for building and deploying interactive web applications.
     - **Implementation:** Used to create a user-friendly interface for inputting queries, displaying responses, and managing multimedia inputs.
   
   - **Markdown:**
     - **Functionality:** Formats and structures text in the application interface.
     - **Implementation:** Used to enhance readability and structure in the Streamlit application's content.

## Pipeline Workflow

1. **Input Acquisition:**
   - Handles various types of input:
     - Voice input converted to text using SpeechRecognition.
     - Textual queries entered directly by the user.
     - Multimedia uploads (images and videos) managed through Streamlit.

2. **Data Preparation:**
   - Processes input data:
     - Audio data handled by PyAudio for voice inputs.
     - Images processed using PIL to prepare them for model input.
     - Videos managed and processed via Streamlit for subsequent operations.

3. **Model Execution:**
   - Utilizes Google's generative AI services (google-generativeai):
     - Receives processed inputs (text, images, videos).
     - Generates responses or content based on the received inputs.

4. **Output Generation:**
   - Converts generated text responses into speech:
     - gTTS used to generate audio output from textual responses.
     - Audio files made available for listening and download through Streamlit.

5. **User Interface:**
   - Streamlit manages the entire workflow:
     - Provides interactive widgets for input handling (text fields, file uploaders).
     - Displays generated responses (text and audio) in a user-friendly interface.
     - Enables multimedia playback and download functionalities.

## User Interface(UI)

![App Screenshot](https://github.com/jhaayush2004/Multimodal-AI-Assistant/blob/main/visuals/UI%20AI.png)

## Running Locally
- Clone the repo .
- Make a virtual environment .
- visit [Google AI Studio](https://ai.google.dev/aistudio) to get your API key .
- Install the dependencies `pip install -r requirements.txt` .
- Run the server `python template.py` .
- Run the server `python setup.py` after changing the information.
- Finally, run the server `python app.py` .
- If facing issues, message me on [LinkedIn](https://www.linkedin.com/in/ayush-shaurya-jha-949732214/?original_referer=https%3A%2F%2Fin%2Elinkedin%2Ecom%2F&originalSubdomain=in) .
## Do visit 
 - [Live demo video of project](https://youtu.be/y87o11ayRFk)
 - [Google’s Gemini 1.5 Pro](https://medium.com/google-cloud/googles-gemini-1-5-pro-revolutionizing-ai-with-a-1m-token-context-window-bfea5adfd35f)
 - [Google AI Studio](https://ai.google.dev/aistudio)
 
Big kudos to **Google DeepMind** 🚀 for crafting this cutting-edge model and championing open-source innovation !!



