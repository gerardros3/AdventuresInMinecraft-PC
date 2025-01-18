from mcpi.minecraft import Minecraft
import openai
from framework.base_bot import BaseBot

mc = Minecraft.create()

class ChatBot(BaseBot):
    def __init__(self):
        super().__init__()

    def answer_question(self, question):
        answers = {
            "What is your name?": "I am OracleBot.",
            "What is the meaning of life?": "42",
            "How are you?": "I am just a bot, but I am functioning properly.",
            "What is the best programming language?": "Python",
            "What is the best game?": "Minecraft",
        }
        answer = answers.get(question, "I don't know the answer to that.")
        self.post_to_chat(answer)

