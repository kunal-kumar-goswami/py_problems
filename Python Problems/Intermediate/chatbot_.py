import random


responses = {
    "hello": ["Hi!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm doing well!", "Great, how about you?"],
    "bye": ["Goodbye!", "See you!", "Take care!"],
}

def chatbot_response(user_input):
    return random.choice(responses.get(user_input.lower(), ["Sorry, I don't understand."]))

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_input))

if __name__ == "__main__":
    chat()
