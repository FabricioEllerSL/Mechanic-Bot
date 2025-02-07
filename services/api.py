from bot import *
from flask import Flask

# Inicializando o bot
chatbot = initialize()

# Criando uma api pra acessar o bot
api_bot = Flask(__name__)

# Rota para responder a uma mensagem do cliente através da api
@api_bot.route("/response/<mensagem>")
def get_response(mensagem):
    response = chatbot.get_response(mensagem)

    print(response)

    return response.text

# Iniciando o server na porta 5000
if __name__ == "__main__":
    api_bot.run()