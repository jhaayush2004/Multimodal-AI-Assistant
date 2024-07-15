def llm_model_image(user_text,path):
    genai.configure(api_key="AIzaSyDqTJiwqE49Sw4xxi44XZBgmlJ5qCHyFtM")
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
