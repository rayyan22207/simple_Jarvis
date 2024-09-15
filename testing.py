import openai
from _key import key_openai

# Set the API key
openai.api_key = key_openai

def get_chatgpt_response(prompt):
    try:
        # Create a chat completion request
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Use a valid model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract and return the message content from the response
        return response.choices[0].message['content']
    except Exception as e:
        # Handle and print exceptions
        print(f"An error occurred: {e}")
        return None

# Example usage
response = get_chatgpt_response("Write a haiku about recursion in programming.")
if response:
    print(response)
