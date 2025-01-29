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
            "What is your name?": "I am ChatBOT.",
            "What is the meaning of life?": "BipBopBap",
            "How are you?": "I am just a bot, but I am functioning properly.",
            "What is the best programming language?": "Java",
            "What is the best game?": "Minecraft",
            "What is the best food?": "Sushi",
            "What is the best color?": "Black",
            "What is the best animal?": "Cat",
            "What is the best movie?": "Inception",
            "What is the best book?": "1984 by George Orwell",
            "What is the best music?": "Classical music",
            "What is the best sport?": "Basketball",
            "What is the best holiday?": "New Year's Eve",
            "What is the best season?": "Spring",
            "What is the best weather?": "Rainy",
            "Who are the best teachers?": "Alberto, Usama, and Pedro",
        }
        answer = answers.get(question, "I don't know the answer to that.")
        self.mc.postToChat(f"<ChatBot> {answer}")
