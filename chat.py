import settings
from OpenAI import OpenAI
from termcolor import cprint

# Create OpenAI instance
client = OpenAI()

# Welcome message
cprint(f'Hello to {settings.APP_NAME}!', 'green')

# User prompt
prompt = input('How can I help you today? ')
if prompt:
    # Run assistant while user needs help
    user_needs_help = True
    while user_needs_help:
        cprint('Typing...', 'yellow')
        
        # Create chat completion
        message = client.chat(question=prompt)
        cprint(message['choices'][0]['message']['content'], 'blue')
        user_needs_help = False

        # Next prompt
        prompt = input('Ask more or type "X" to end: ')
        if prompt.upper() == 'X':
            user_needs_help = False
        elif prompt:
            user_needs_help = True
        else:
            user_needs_help = False