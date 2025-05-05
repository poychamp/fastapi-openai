from dotenv import dotenv_values
import openai

config = dotenv_values(".env")

openai_client = openai.Client(api_key=config['OPENAI_API_KEY'])