!pip install chatterbot chatterbot_corpus

# Import the necessary modules
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('WaterBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Define a function for the chatbot interaction
def chat_with_bot():
    print("WaterBot: Hello! I'm here to help with water body cleanliness. Ask me anything.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("WaterBot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print("WaterBot:", response)

# Start the chatbot interaction
chat_with_bot()
