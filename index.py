import settings
from OpenAI import OpenAI

# Create OpenAI instance
client = OpenAI()

# Welcome message
print(f'Hello to {settings.APP_NAME}!')

# User prompt
prompt = input('How can I help you today? ')
if prompt:
    # Run assistant while user needs help
    user_needs_help = True
    while user_needs_help:
        print('Typing...')
        if not client.thread_id:
            # Create a Thread
            client.create_thread()
        # Add a Message to a Thread
        client.add_message_to_thread(question=prompt)
        # Run the Assistant
        client.run_assistant()

        # Check the Run status
        message_id = ""
        while client.check_run_status() == 'in_progress':
            # Display the Assistant's Response
            res = client.display_assistant_response()
            message_id = res['first_id']
            user_needs_help = False

        # Retrieve message
        message = client.retrieve_message(message_id)
        for item in message['content']:
            print(item['text']['value'])

        # Next prompt
        prompt = input('Ask more or type "X" to end: ')
        if prompt.upper() == 'X':
            user_needs_help = False
        elif prompt:
            user_needs_help = True
        else:
            user_needs_help = False