from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

# Lista contendo os caminhos dos arquivos JSON que armazenam conversas para treinamento
CONVERSATIONS = [
    "./data/greetings.json",
    "./data/basic_infos.json"
]

def initialize():
    """
    Inicializa o chatbot e retorna um treinador para ele.
    
    - Cria um chatbot chamado "Mechanic Robot".
    - Instancia um treinador do tipo ListTrainer para esse chatbot.
    - Retorna o treinador para ser usado no treinamento.
    """
    bot = ChatBot("Mechanic Robot")  # Criando uma instância do chatbot
    trainer = ListTrainer(bot)       # Criando um treinador baseado em listas

    return trainer  # Retorna o treinador para uso posterior

def load_conversations():
    """
    Carrega as conversas dos arquivos JSON especificados na variável CONVERSATIONS.
    
    - Lê cada arquivo da lista e carrega o conteúdo JSON.
    - Extrai as conversas do dicionário JSON e as adiciona a uma lista.
    - Retorna uma lista contendo todas as conversas carregadas.
    """
    conversations = []  # Lista onde serão armazenadas as conversas

    for conversation_file in CONVERSATIONS:  # Percorre os arquivos na lista CONVERSATIONS
        with open(conversation_file, "r") as file:  # Abre o arquivo JSON no modo leitura
            training_conversations = json.load(file)  # Carrega o conteúdo JSON como um dicionário
            conversations.append(training_conversations["conversations"])  # Adiciona as conversas à lista
            
            file.close()  # Fecha o arquivo (desnecessário, pois o "with" já gerencia isso)

    return conversations  # Retorna a lista de conversas

def train(trainer, conversations):
    """
    Treina o chatbot com as conversas carregadas.
    
    - Percorre todas as conversas e extrai os pares de mensagens e respostas.
    - Exibe uma mensagem indicando que o chatbot está sendo treinado.
    - Para cada mensagem em um par, treina o bot associando-a à resposta correspondente.
    """
    for conversation in conversations:  # Percorre a lista de conversas
        for message_response in conversation:  # Percorre cada interação dentro da conversa
            messages = message_response["messages"]  # Obtém a lista de mensagens
            response = message_response["response"]  # Obtém a resposta correspondente

            print(f"Training robot...")  # Mensagem indicando que o treinamento está acontecendo
            for message in messages:  # Para cada mensagem na interação
                trainer.train([message, response])  # Treina o chatbot com o par (mensagem, resposta)

if __name__ == "__main__":
    trainer = initialize()  # Inicializa o treinador

    conversations = load_conversations()  # Carrega as conversas dos arquivos JSON
    if conversations:  # Se houver conversas disponíveis
        train(trainer, conversations)  # Treina o chatbot com os dados carregados
