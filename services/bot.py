from chatterbot import ChatBot
from difflib import SequenceMatcher

MINIMUM_TRUST = 0.60


def compare_messages(typed_message, candidate_message):
    confidence = 0.0

    typed_text = typed_message.text
    candidate_text = candidate_message.text
    if typed_text and candidate_text:
        confidence = SequenceMatcher(None, 
            typed_text,
            candidate_text)
        confidence = round(confidence.ratio(), 2)

    return confidence


def initialize():
    bot = ChatBot("IFBA Service Bot",
                  read_only=True,
                #    statement_comparison_function=compare_messages,     
                  logic_adapters=[
                      {
                          "import_path": "chatterbot.logic.BestMatch"
                      }
                  ])

    return bot


def run_bot(bot):
    while True:
        message = input("Type something... \n")
        response = bot.get_response(message.lower())
        print(f"Confidence value: {response.confidence}")
        if response.confidence >= MINIMUM_TRUST:
            print(">>", response.text)
        else:
            print("Unfortunately, I don't know how to answer that yet.")
            print("Please ask something else.")


if __name__ == "__main__":
    bot = initialize()
    run_bot(bot)
