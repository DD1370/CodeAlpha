def chatbot():
    print("🤖 Welcome to Basic Chatbot!")
    print("You can say: hello, how are you, bye\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user_input == "how are you?":
            print("Bot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
