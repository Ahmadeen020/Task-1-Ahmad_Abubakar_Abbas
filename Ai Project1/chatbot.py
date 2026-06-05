responses = {
    'hello': 'Hi there!',
    'hi': 'Hello!',
    'how are you?': 'I am doing well, thanks for asking!',
    'help': 'I can only respond to greetings and exit commands.',
    'bye': 'Goodbye!'
}

# The Professional Approach
while True:
    user_input = input('YOU: ')
    clean_input = user_input.lower().strip()
    if clean_input == 'exit':
        print('Bot: Goodbye!')
        break

    reply = responses.get(clean_input, 'I do not understand.')
    print("Bot:", reply)