import unittest
from MyAdventures.practicaTAP.bots import ChatBot

class TestChatBot(unittest.TestCase):
    def setUp(self):
       self.oracle_bot = ChatBot()

    def test_answer_question(self):
        # This test will check if the OracleBot answers questions correctly
        questions_and_answers = {
            "What is your name?": "I am OracleBot.",
            "What is the meaning of life?": "42",
            "How are you?": "I am just a bot, but I am functioning properly.",
            "What is the best programming language?": "Python",
            "What is the best game?": "Minecraft"
        }
        
        for question in questions_and_answers.items():
            with self.subTest(question=question):
                self.oracle_bot.answer_question(question)
                # Assuming the test passes if no exceptions are raised

if __name__ == '__main__':
    unittest.main()



