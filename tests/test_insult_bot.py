import unittest
from MyAdventures.practicaTAP.bots import InsultBot


class TestInsultBot(unittest.TestCase):
    def setUp(self):
        self.insult_bot = InsultBot()

    def test_insult(self):
        # This test will check if the insults are posted to the chat
        self.insult_bot.insult()

if __name__ == '__main__':
    unittest.main()

