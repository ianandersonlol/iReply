# iReply

This script utilizes OpenAI's GPT-3.5-turbo model to generate responses to the latest received iMessage and send the response back to the sender. It's an automated iMessage assistant that reads the latest message, generates a response, and sends it back to the sender on your behalf.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Setting up Open AI Developer Account and API Key](#Setting_Up_OpenAI_Developer_Account_and_API_Key)
- [Usage](#usage)

## Requirements

- Python 3
- `openai` library
- iMessage account
- macOS

## Setup

1. Install the `openai` library:

```bash
pip install openai
```

2. Replace `your-openai-api-key` with your OpenAI API key:

```python
openai.api_key = 'your-openai-api-key'
```

3. Replace `YOUR_APPLE_ID@icloud.com` with your Apple ID email:

```applescript
set myBuddy to a buddy "{to}" of service "E:YOUR_APPLE_ID@icloud.com"
```
## Setting Up OpenAI Developer Account and API Key

1. Visit the OpenAI website at [https://www.openai.com/](https://www.openai.com/).
2. Click on the "Sign Up" button and create an account.
3. After verifying your email address and logging in, navigate to the API section.
4. In the API section, you will find your API key. Copy this key and keep it safe; you'll need it for the next step.

## Usage

1. Run the script:

```bash
python imessage_assistant.py
```

The script will perform the following actions:

- Read the latest iMessage received.
- Generate a response using GPT-3.5-turbo.
- Send the generated response back to the sender.

### Functions

- `read_latest_imessage()`: Reads the latest iMessage from the `chat.db` database and returns the message text and sender's handle ID.
- `generate_response(message)`: Generates a response using OpenAI's GPT-3.5-turbo model based on the provided message.
- `send_imessage(to, message)`: Sends the generated response to the specified iMessage handle ID.
- `main()`: Combines the above functions to read the latest iMessage, generate a response, and send it back to the sender.

**Note**: The script is designed to run on macOS, as it uses the iMessage app and system-specific libraries. The generated response is signed with "BinkyBonky" to indicate that it's from the AI bot and not the user. Also it has no context of your conversation... so expect hilarity. 
