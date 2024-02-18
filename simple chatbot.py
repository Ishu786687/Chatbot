import nltk
from nltk.chat.util import Chat, reflections


patterns = [
    (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I am fine, how about you?']),
    (r'what is your name', ['I am a chatbot. You can call me annie.']),
    (r'quit|exit', ['Goodbye!', 'Bye!']),
]


chatbot = Chat(patterns, reflections)


def chatbot_interaction():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    chatbot_interaction()
