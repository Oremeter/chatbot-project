
import os
import openai
import chainlit as cl
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get OpenAI API Key from environment
openai_api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = openai_api_key

@cl.on_message
async def main(message: cl.Message):
    """
    Chainlit chatbot handler. Receives user input and returns OpenAI response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model
            messages=[{"role": "user", "content": message.content}],
            max_tokens=50, 
            temperature=0.7
        )

        bot_response = response.choices[0].message['content'].strip()

        # Send the response to the user
        await cl.Message(content=bot_response).send()

    except Exception as e:
        await cl.Message(content=f"Error: {str(e)}").send()

if __name__ == "__main__":
    cl.run(
        host="0.0.0.0",   
        port=8505,           
        root_path="/chatbot"  
    )