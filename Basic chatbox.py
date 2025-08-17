def chatbot_reply(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

def run_chatbot():
    print("Welcome to the Chatbot! (type 'bye' to exit)")
    while True:
        user_message = input("You: ")
        reply = chatbot_reply(user_message)
        print("Bot:", reply)
        if user_message.lower() == "bye":
            break

# Start the chatbot
run_chatbot()
