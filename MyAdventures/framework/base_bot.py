import mcpi.minecraft as Minecraft
from threading import Thread
from hugchat import hugchat
from hugchat.login import Login
from bots.tnt_bot import TntBOT
from bots.chat_bot import ChatBOT
from bots.insult_bot import InsultBOT


# main abstract class for a bot
class Bot():
    def __init__(self, entity):
        self.mc = Minecraft.Minecraft.create()   # minecraft Minecraft server connection
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
            
    # Function for generating bot response
    def generate_response(prompt_input, email, passwd):
        sign = Login(email, passwd)
        cookies = sign.login()
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        return chatbot.chat(prompt_input)
    
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
                self.tnt_bot_list[player] = TntBOT(player)
                self.chat_ai_bot_list[player] = ChatBOT(player)
                self.insult_bot_list[player] = InsultBOT(player)
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
            
            
            # Usar map() con una lambda para crear las listas de bots por tipo
            #self.tnt_bot_list = dict(map(lambda entity: (entity, TNT(entity)), self.player_list))
            #self.chat_ai_bot_list = dict(map(lambda entity: (entity, ChatAI(entity)), self.player_list))
            #self.insult_bot_list = dict(map(lambda entity: (entity, Insult(entity)), self.player_list))

    
    def get_bot_list(self, bot_type):
        """Obtiene la lista de bots del tipo especificado."""
        
        print(f"Received bot type: {bot_type}")
        if bot_type == 'TNT'.casefold():
            return self.tnt_bot_list
        elif bot_type == 'ChatAI'.casefold():
            return self.chat_ai_bot_list
        elif bot_type == 'Insult'.casefold():
            return self.insult_bot_list
        else:
            raise ValueError("Invalid bot type")
    
    
    def printLists(self):
        print("Player list = "+str(self.player_list))
        print("TNT list = "+str(self.tnt_bot_list))
        print("GPT list = "+str(self.chat_ai_bot_list))
        print("Insult list = "+str(self.insult_bot_list))