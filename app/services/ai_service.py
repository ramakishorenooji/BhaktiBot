import openai
from app.config import OPENAI_API_KEY

def generate_wish(name: str, festival: str) -> str:
    """Generate a personalized festival wish using OpenAI GPT"""
    openai.api_key = OPENAI_API_KEY
    prompt = f"Write a warm and friendly festival wish for {name} on the occasion of {festival}."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Updated model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"