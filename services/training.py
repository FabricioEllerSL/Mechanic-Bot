from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONVERSATIONS = [
    "./data/greetings.json",
    "./data/basic_information.json"
]

def initialize():
    bot = ChatBot("Mechanic Robot")
    trainer = ListTrainer(bot)

    return trainer

def load_conversations():
    conversations = []

    for conversation_file in CONVERSATIONS:
        with open(conversation_file, "r") as file:
            training_conversations = json.load(file)
            conversations.append(training_conversations["conversations"])

            file.close()

    return conversations

def train(trainer, conversations):
    for conversation in conversations:
        for message_response in conversation:
            messages = message_response["messages"]
            response = message_response["response"]

            print(f"Training robot...")
            for message in messages:
                trainer.train([message, response])


if __name__ == "__main__":
    trainer = initialize()

    conversations = load_conversations()
    if conversations:
        train(trainer, conversations)
