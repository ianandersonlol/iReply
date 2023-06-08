import openai
import sqlite3
from imessage_reader import Reader
import os
import subprocess

# Set OpenAI API key
openai.api_key = 'your-openai-api-key'

def read_latest_imessage():
    # Set path to chat.db
    path_to_db = os.path.expanduser('~/Library/Messages/chat.db')

    # Connect to the database
    conn = sqlite3.connect(path_to_db)

    # Create a reader
    reader = Reader(conn)

    # Get the latest message
    messages = reader.get_messages(limit=1)

    # Close the connection
    conn.close()

    # Return the text of the latest message
    return messages[0].text, messages[0].handle_id

def generate_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistan that generates responses to text messages! Sign all responses from BinkyBonky so they know you are a bot and not me."},
            {"role": "user", "content": message},
        ],
        max_tokens=300
    )

    return response.choices[0].message['content']

def send_imessage(to, message):
    applescript = f'''
    tell application "Messages"
        set myBuddy to a buddy "{to}" of service "E:YOUR_APPLE_ID@icloud.com"
        send "{message}" to myBuddy
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript])

def main():
    latest_message, sender = read_latest_imessage()
    print(f"Latest message: {latest_message}")

    response = generate_response(latest_message)
    print(f"Generated response: {response}")

    send_imessage(sender, response)

if __name__ == "__main__":
    main()
