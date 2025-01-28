from email.policy import default
import mcpi.minecraft as game
import mcpi.block as blocks
import mcpi.entity as entities
import mcpi.event as events
import random
import time
from threading import Thread

# main abstract class for a bot
class Bot():
    def __init__(self, entity):
        self.mc = game.Minecraft.create()   # minecraft game server connection
        self.entity = entity    # player who called the function
        self.control = None     # control variable for main loop in bot function
        self.t1 = Thread        # declaration of a thread for the bot (needs to be updated by the specific bot)
        self.player_name = self.mc.entity.getName(self.entity)
    
    # main function to start a thread with the bot
    def begin(self):
        if(not self.t1.is_alive()):
            self.control = True
            self.t1.start()
            self.mc.postToChat(f"§2<{self.name}> ***The bot has been enabled for {self.player_name}!!")
        else:
            self.mc.postToChat(f"§2<{self.name}> ***The bot is already running for {self.player_name}!!")
    
    # main function to stop the bot thread
    def stop(self):
        if(self.t1.is_alive()):
            self.control = False
            self.t1.join()
            self.mc.postToChat(f"§2<{self.name}> ***The bot has been disabled for {self.player_name}!!")
        else:
            self.mc.postToChat(f"§2<{self.name}> ***The bot is not running yet for {self.player_name}!!")
        
        
# specific bot class to spawn TNT near the player
class TNT(Bot):
    def __init__(self, entity):
        super().__init__(entity)  # inherit attributes
        self.name = "TNTBot"    # name of this specific bot
        self.t1 = Thread(target=self._main) # update thread with the function to execute
        self.counter = 0
        
    # specific function of the TNT bot
    def _main(self):
        while(self.control):    # run while the bot is enabled
            if self.counter > 0:
                time.sleep(1)
                self.counter = self.counter - 1
            else:
                self.counter = random.randint(3, 15)
                # spawn TNT once in a random interval between 3 and 15 seconds
                pos = self.mc.entity.getTilePos(self.entity)    # Get player position
                self.mc.spawnEntity(pos.x, pos.y+2, pos.z, entities.PRIMED_TNT.id)   # Spawn an ignited TNT on top of the player

# Main ChatAI Bot Class
class ChatAI(Bot):
    def __init__(self, entity):
        super().__init__(entity)
        self.name = "ChatAI"  # Name of the bot
        self.t1 = Thread(target=self._main)  # Update thread with the function to execute
        self.bot_entity_id = self.t1.name
        self.player_name = self.mc.entity.getName(self.entity)

    # Main function for the ChatAI bot (to process commands)
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

class Insult(Bot):
    def __init__(self, entity):
        super().__init__(entity)
        self.name = "InsultBot"  # Name of the bot
        self.t1 = Thread(target=self._main)  # Update thread with the function to execute
        self.bot_entity_id = self.t1.name
        self.player_name = self.mc.entity.getName(self.entity)
     

    # Main function for the Insult bot (to process commands)
    def _main(self):
        while self.control:
            chatEvents = self.mc.events.pollChatPosts()
            
            for command in chatEvents:
                text = str(command.message) # Convert chat event to str
                sender_entity_id = command.entityId
                if sender_entity_id == self.bot_entity_id:
                    continue
                
                if(not text.startswith(":") and not text.startswith("<")):
                    self.insult_command("Generate low insults for this player: "+ self.player_name)


    # Function to handle insults
    def insult_command(self, prompt):
        try:
            self.insults = [
            "You're as bright as a black hole!",
            "I've seen smarter rocks.",
            "You bring everyone so much joy... when you leave the room."
            "You're not pretty enough to be this stupid.",
            "I'd agree with you but then we'd both be wrong.",
            "You're so dumb, you'd think a rock was a good idea.",
            "You're not even a good liar.",
            "I'm not saying you're stupid, but you're not saying anything either.",
            "You're so stupid, you'd think a toilet was a good place to take a bath.",
            "You're not the dumbest person in the world, but you better hope they don't die.",
            "You're so dumb, you'd trip over a wireless connection.",
            "You're not the sharpest tool in the shed, but you're definitely a tool.",
            "You're so dumb, you'd think a quarterback was a refund.",
            "You're not the brightest crayon in the box, but you're still a crayon.",
            "You're so dumb, you'd think a quarterback was a refund."
        ]
            insult = random.choice(self.insults)
            self.mc.postToChat(f"<InsultBot> {insult}")
        except Exception as e:
            self.mc.postToChat(f"<InsultBot> Error: {str(e)}")

class BotManager:
    __instance = None
    player_list = []
    tnt_bot_list = {}
    chat_ai_bot_list = {}
    insult_bot_list = {}
    
    @staticmethod
    def getInstance():
        if BotManager.__instance == None:
            BotManager()
        return BotManager.__instance
    
    def __init__(self):
        if BotManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            BotManager.__instance = self
    

    def update_player_list(self, mc):
        """Actualiza las listas de jugadores y bots para cada jugador."""
        new_player_list = mc.getPlayerEntityIds()
        if len(new_player_list) > len(self.player_list):
            diff = list(set(new_player_list).difference(self.player_list))
            self.player_list.extend(diff)
            for player in diff:
                self.tnt_bot_list[player] = TNT(player)
                self.chat_ai_bot_list[player] = ChatAI(player)
                self.insult_bot_list[player] = Insult(player)
            self.printLists()
        
        elif len(new_player_list) < len(self.player_list):
            diff = list(set(self.player_list).difference(new_player_list))
            self.player_list = new_player_list  #[x for x in self.player_list if x in new_player_list]
            for player in diff:
                self.tnt_bot_list[player].stop()
                del self.tnt_bot_list[player]
                
                self.chat_ai_bot_list[player].stop()
                del self.chat_ai_bot_list[player]
                
                self.insult_bot_list[player].stop()
                del self.insult_bot_list[player]
            self.printLists()
            
            
    
    def get_bot_list(self, bot_type):
        """Obtiene la lista de bots del tipo especificado."""
        
        print(f"Received bot type: {bot_type}")
        switcher = {
            'TNT'.casefold(): self.tnt_bot_list,
            'ChatAI'.casefold(): self.chat_ai_bot_list,
            'Insult'.casefold(): self.insult_bot_list
        }
        return switcher.get(bot_type.casefold(), None)

    
    
    def printLists(self):
        print("Player list = "+str(self.player_list))
        print("TNT list = "+str(self.tnt_bot_list))
        print("GPT list = "+str(self.chat_ai_bot_list))
        print("Insult list = "+str(self.insult_bot_list))