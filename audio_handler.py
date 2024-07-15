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
