def llm_model_video(user_text, video_path):
    genai.configure(api_key="AIzaSyA1OEqsguS7WhhWY9ERqpTZRWNyq14oWFk")
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
