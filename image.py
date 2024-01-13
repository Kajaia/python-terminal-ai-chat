import settings
from OpenAI import OpenAI
from termcolor import cprint

# Create OpenAI instance
client = OpenAI()

# Welcome message
cprint(f'Hello to {settings.APP_NAME}!', 'green')

# User prompt
prompt = input('What do you want to generate? ')
if prompt:
    # Run assistant while user needs help
    user_needs_help = True
    while user_needs_help:
        cprint('Generating... It will take some time.', 'yellow')
        
        # Create image
        res = client.create_image(prompt)
        image = res['data'][0]
        cprint(image['revised_prompt'], 'blue')
        cprint(image['url'], 'red')
        user_needs_help = False