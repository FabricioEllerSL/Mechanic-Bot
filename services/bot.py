from chatterbot import ChatBot
from difflib import SequenceMatcher

MINIMUM_TRUST = 0.60

def compare_messages(typed_message, candidate_message):
    """
    Compara a mensagem digitada pelo usuário com uma possível resposta do chatbot.
    Retorna um valor de confiança entre 0 (sem semelhança) e 1 (mensagens idênticas).
    """
    confidence = 0.0  # Inicializa o nível de confiança com 0

    # Obtém o texto das mensagens digitadas pelo usuário e da resposta candidata
    typed_text = typed_message.text
    candidate_text = candidate_message.text

    # Se ambas as mensagens não estiverem vazias
    if typed_text and candidate_text:
        # Usa o SequenceMatcher para calcular a similaridade entre as duas mensagens
        confidence = SequenceMatcher(None, 
            typed_text,
            candidate_text)
        # Arredonda a confiança para duas casas decimais
        confidence = round(confidence.ratio(), 2)

    return confidence  # Retorna o valor de confiança calculado


def initialize():
    """
    Inicializa o chatbot com um nome e configurações específicas.
    - O chatbot é configurado com o adaptador 'BestMatch', que tenta encontrar a melhor resposta possível.
    - A comparação de mensagens está desativada no momento, mas a função compare_messages poderia ser usada aqui.
    """
    bot = ChatBot("IFBA Service Bot",  # Nome do chatbot
                  read_only=True,       # O bot é apenas de leitura (não aprende com interações)
                #    statement_comparison_function=compare_messages,  # Descomentando isso permitiria usar a função de comparação personalizada
                  logic_adapters=[  # Lista de adaptadores de lógica para o chatbot
                      {
                          "import_path": "chatterbot.logic.BestMatch"  # Adaptador que escolhe a melhor correspondência de resposta
                      }
                  ])

    return bot  # Retorna o chatbot configurado


def run_bot(bot):
    """
    Executa o chatbot, permitindo que o usuário interaja com ele em tempo real.
    O bot responde à entrada do usuário e verifica se a confiança na resposta é suficiente.
    """
    while True:  # O loop continua executando até que o programa seja interrompido
        # Solicita ao usuário que digite uma mensagem
        message = input("Type something... \n")
        
        # Obtém a resposta do chatbot para a mensagem digitada, convertendo para minúsculas
        response = bot.get_response(message.lower())
        
        # Exibe o valor de confiança da resposta
        print(f"Confidence value: {response.confidence}")
        
        # Verifica se o valor de confiança da resposta é maior ou igual ao mínimo exigido
        if response.confidence >= MINIMUM_TRUST:
            # Se a confiança for suficiente, exibe a resposta do bot
            print(">>", response.text)
        else:
            # Se a confiança for insuficiente, exibe uma mensagem dizendo que o bot não sabe a resposta
            print("Unfortunately, I don't know how to answer that yet.")
            print("Please ask something else.")


if __name__ == "__main__":
    """
    Inicializa o chatbot e executa a função de interação contínua.
    """
    bot = initialize()  # Inicializa o chatbot
    run_bot(bot)        # Executa o bot, permitindo que o usuário interaja com ele
