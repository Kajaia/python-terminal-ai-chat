from ChatGPT import ChatGPT
import settings

# Create ChatGPT instance
chat = ChatGPT()

# Welcome message
print(f'Hello to {settings.APP_NAME} Chat!')

# User prompt
prompt = input('How can I help you today? ')
if prompt:
    user_needs_help = True
    while user_needs_help:
        print('Typing...')
        if not chat.thread_id:
            # Create a Thread
            chat.create_thread()
        # Add a Message to a Thread
        chat.add_message_to_thread(question=prompt)
        # Run the Assistant
        chat.run_assistant()
        # Check the Run status
        message_id = ""
        while chat.check_run_status() == 'in_progress':
            # Display the Assistant's Response
            res = chat.display_assistant_response()
            message_id = res['first_id']
            user_needs_help = False
        # Retrieve message
        message = chat.retrieve_message(message_id)
        for item in message['content']:
            print(item['text']['value'])
        # Next prompt
        prompt = input('Ask more or type "X" to stop chat: ')
        if prompt.upper() == 'X':
            user_needs_help = False
        elif prompt:
            user_needs_help = True
        else:
            user_needs_help = False