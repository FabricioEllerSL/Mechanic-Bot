from bot import *
from flask import Flask

chatbot = initialize()
api_bot = Flask(__name__)

@api_bot.route("/resposta/<mensagem>")
def get_resposta(mensagem):
    resposta = chatbot.get_response(mensagem)

    print(resposta)

    return resposta.text

if __name__ == "__main__":
    api_bot.run()