from framework.read_chat import *
from framework.base_bot import Bot
from threading import Thread


# Main ChatBOT Bot Class
class ChatBOT(Bot):
    def __init__(self, entity):
        super().__init__(entity)
        self.name = "ChatBOT"  # Name of the bot
        self.t1 = Thread(target=self._main)  # Update thread with the function to execute
        self.bot_entity_id = self.t1.name
        self.player_name = self.mc.entity.getName(self.entity)

    # Main function for the ChatBOT bot (to process commands)
    def _main(self):
        while self.control:
            chatEvents = self.mc.events.pollChatPosts()
        
            for command in chatEvents:
                text = str(command.message) # Convert chat event to str
                sender_entity_id = command.entityId
                if sender_entity_id == self.bot_entity_id:
                    continue
                    
                if text.endswith("?"):
                    self.answer_question(text)

    # Function to handle GPT prompts
    def answer_question(self, question):
        answers = {
            "What is your name?": "I am OracleBot.",
            "What is the meaning of life?": "Beer",
            "How are you?": "I am just a bot, but I am functioning properly.",
            "What is the best programming language?": "Python",
            "What is the best game?": "Minecraft",
            "What is the best food?": "Pizza",
            "What is the best color?": "Blue",
            "What is the best animal?": "Dog",
            "What is the best movie?": "The Matrix",
            "What is the best book?": "The Lord of the Rings",
            "What is the best music?": "Rock music",
            "What is the best sport?": "Soccer",
            "What is the best holiday?": "Christmas",
            "What is the best season?": "Summer",
            "What is the best weather?": "Sunny",
            "Who are the best teachers?": "Usama, Pedro and Alberto",
        }
        answer = answers.get(question, "I don't know the answer to that.")
        self.mc.postToChat(f"<ChatBot> {answer}")
