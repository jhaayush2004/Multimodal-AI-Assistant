import streamlit as st
from src.helper import voice_input, llm_model_audio, llm_model_image, llm_model_video, text_to_speech

def main():
  
    st.title("Multilingual AI Assistant")

    st.sidebar.title("Select Model")
    model_choice = st.sidebar.radio("Choose Model", ("Text Only", "Image and Text", "Video and Text"))

    if model_choice == "Text Only":
        if st.button("Ask me anything"):
            with st.spinner("Listening..."):
                text = voice_input()
                response = llm_model_audio(text)
                text_to_speech(response)

                audio_file = open("speech.mp3", "rb")
                audio_bytes = audio_file.read()

                st.text_area(label="Response:", value=response, height=350)
                st.audio(audio_bytes)
                st.download_button(label="Download Speech",
                                   data=audio_bytes,
                                   file_name="speech.mp3",
                                   mime="audio/mp3")

    elif model_choice == "Image and Text":
        uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'], key="image_uploader")
        if uploaded_file is not None:
            image_path = f"temp_image.{uploaded_file.type.split('/')[1]}"
            with open(image_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            
            user_text = st.text_input("Enter your query:")

            if "text1" not in st.session_state:
                st.session_state.text1 = ""

            if st.button("Ask me anything", key="voice_button"):
                with st.spinner("Listening..."):
                    st.session_state.text1 = voice_input()  # Capture voice input
            
            final_query = f"{st.session_state.text1} and {user_text}" if st.session_state.text1 else user_text
                
            st.write("Final query:", final_query)
            if st.button("Generate Response", key="generate_button"):
                response = llm_model_image(final_query, image_path)
                response_clean = response.replace('*', '')
                st.text_area(label="Response:", value=response_clean, height=350)
                text_to_speech(response_clean)  # Generate speech from text response
                st.audio(open("speech.mp3", "rb").read(), format='audio/mp3')  # Play the generated speech
                st.download_button(label="Download Speech", data=open("speech.mp3", "rb").read(), file_name="speech.mp3")

    elif model_choice == "Video and Text":
        video_file = st.file_uploader("Upload Video", type=['mp4'], key="video_uploader")
        if video_file is not None:
            video_path = f"temp_video.mp4"
            with open(video_path, "wb") as f:
                f.write(video_file.read())
            
            user_text = st.text_input("Enter your query:")
            
            if "text2" not in st.session_state:
                st.session_state.text2 = ""
    
            if st.button("Ask me anything", key="voice_button"):
                with st.spinner("Listening..."):
                    st.session_state.text2 = voice_input()  # Capture voice input
            
            final_query = f"{st.session_state.text2} and {user_text}" if st.session_state.text2 else user_text
            
            st.write("Final query:", final_query)
            
            if st.button("Generate Response", key="video_generate_button"):
                response = llm_model_video(final_query, video_path)
                
                # Remove asterisks from the response
                response_clean = response.replace('*', '')
                
                st.text_area(label="Response:", value=response_clean, height=350)
                text_to_speech(response_clean)
                st.audio("speech.mp3", format='audio/mp3')
                st.download_button(label="Download Speech", data=open("speech.mp3", "rb").read(), file_name="speech.mp3")


if __name__ == "__main__":
    main()
