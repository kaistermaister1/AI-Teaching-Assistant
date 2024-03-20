from flask import Flask, render_template, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key='--',)

# This file contains the prompt for ChatGPT, and is updated when the professor enters a new topic
prompt_file = 'upload/upload.txt'

# Writes the topic to the txt file, and returns the final prompt. Topic is the type of video clips the professor requests
def update_topic(topic):
    # Read the existing content of the file
    with open(prompt_file, 'r') as file:
        lines = file.readlines()

    # Modify content by updating topic
    lines[0 - 3:] = topic

    # Write the modified content back to the file
    with open(prompt_file, 'w') as file:
        file.writelines(lines)
        return file.read()

# Calls GPT to create a more search-friendly prompt for Youtube. See upload.txt for more info
def generate_search(prompt):
    # Create a chat completion with the file content as the user's message
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
        ],
        model="gpt-3.5-turbo",
    )

    # Extract the generated text from the API response
    generated_text = chat_completion.choices[0].message.content


if __name__ == '__main__':
    app.run(debug=True)