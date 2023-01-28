
# APIAI - Telegram Bot

This is a Telegram bot that can interact with users in a natural language and respond to their messages. It uses the Dialogflow API to understand and respond to user inputs. The bot is written in Python and uses the python-telegram-bot library to interact with the Telegram API. 

## Getting Started

To get started with the bot, you will need to:

1. **Create a Telegram bot**: Talk to the [BotFather](https://t.me/BotFather) on Telegram to create a new bot and obtain a bot token.

2. **Create a Dialogflow project**: Create a new project on Dialogflow, a Google-owned developer of human–computer interaction technologies based on natural language conversations. And obtain a client access token.

3. **Replace the tokens**: Replace the placeholder values for `TOKEN` and `access_token` in the code with the actual tokens obtained from Telegram and Dialogflow respectively.

4. **Run the script**: Run the script using the command `python bot.py`

## Using the Bot

- The bot will listen for the `/start` command and respond with "Hello, let's talk?".
- When the user types any message, the bot will process the message using the Dialogflow API and generate a response.
- If Dialogflow is unable to generate a response, the bot will reply with "Sorry, I didn't understand that."

## Prerequisites

- Make sure that you have python and pip installed on your system
- Use the following command to install the required libraries 
```
pip install python-telegram-bot
pip install apiai
```
## Note

- Don't share you tokens online.
- If you face any issues, please let me know.
