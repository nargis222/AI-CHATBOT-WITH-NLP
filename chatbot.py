import nltk
from nltk.chat.util import Chat, reflections

# Download required resources
nltk.download('punkt')

# Define patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created using NLTK.",]
    ],
    [
        r"how are you ?",
        ["I'm just a bunch of code, but I'm doing great!", "All systems operational!"]
    ],
    [
        r"(.*) your name ?",
        ["You can call me NLPBot.",]
    ],
    [
        r"what do you do ?",
        ["I answer questions and help users with basic queries.",]
    ],
    [
        r"(.) help (.)",
        ["Sure, I'm here to help! Please tell me your question.",]
    ],
    [
        r"quit",
        ["Bye for now!", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["Sorry, I don't understand that. Could you rephrase?"]
    ],
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hi! I'm an NLP chatbot. Type 'quit' to exit.")
chatbot.converse()
