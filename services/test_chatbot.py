import unittest
from bot import *

class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.bot = initialize()

    def test_about_car(self):
        messages = [
            "Qual a frequência de troca de óleo do meu veículo?",
            "Como saber as especificações do pneu?",
            "Qual a amperagem de uma bateria de carro?",
            "Como fazer a troca de óleo do veículo?",
            "Por que carros possuem diferentes combustíveis?",
        ]

        for message in messages:
            response = self.bot.get_response(message)
            print(response.confidence)
            self.assertGreaterEqual(response.confidence, MINIMUM_TRUST)

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = unittest.TestSuite()

    tests.addTest(loader.loadTestsFromTestCase(TestChatbot))

    runner = unittest.TextTestRunner()
    runner.run(tests)
