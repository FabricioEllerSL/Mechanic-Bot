import unittest
from bot import *


# A classe TestChatbot contém os testes que serão realizados no chatbot.
class TestChatbot(unittest.TestCase):

    # O método setUp é executado antes de cada teste, configurando o ambiente necessário.
    def setUp(self):
        """
        Inicializa o chatbot para ser usado em cada um dos testes.
        A função initialize() do código 'bot.py' cria e retorna um treinador para o chatbot.
        """
        self.bot = initialize()  # Chama a função initialize() que retorna o treinador e armazena na variável self.bot

    def test_about_car(self):
        """
        Testa o chatbot em relação a perguntas sobre carros, garantindo que ele forneça respostas adequadas
        com uma confiança mínima exigida (MINIMUM_TRUST).
        """
        # Lista de mensagens (perguntas) que serão enviadas para o chatbot durante o teste
        messages = [
            "Qual a frequência de troca de óleo do meu veículo?",
            "Como saber as especificações do pneu?",
            "Qual a amperagem de uma bateria de carro?",
            "Como fazer a troca de óleo do veículo?",
            "Por que carros possuem diferentes combustíveis?",
        ]

        # Itera sobre cada uma das mensagens na lista 'messages'
        for message in messages:
            # Envia a mensagem para o chatbot e obtém a resposta
            response = self.bot.get_response(message)
            # Exibe a resposta no terminal para visualização
            print(response, '\n')
            # Verifica se o nível de confiança da resposta é maior ou igual ao valor mínimo exigido
            self.assertGreaterEqual(response.confidence, MINIMUM_TRUST)

# Este bloco de código é executado quando o script é chamado diretamente.
if __name__ == "__main__":
    """
    Cria um conjunto de testes, carrega os testes da classe TestChatbot e executa os testes.
    """
    loader = unittest.TestLoader()  # Carrega os testes automatizados (casos de teste)
    tests = unittest.TestSuite()    # Cria um conjunto de testes

    # Adiciona os testes da classe TestChatbot ao conjunto de testes
    tests.addTest(loader.loadTestsFromTestCase(TestChatbot))

    # Cria um runner para executar os testes e exibe os resultados no terminal
    runner = unittest.TextTestRunner()
    runner.run(tests)  # Executa os testes e exibe os resultados
