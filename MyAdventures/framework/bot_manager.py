from bots.tnt_bot import TNT as tnt
from bots.chat_bot import ChatBOT as gpt
from bots.insult_bot import Insult


class bot_manager:
    __instance = None
    player_list = []
    tnt_bot_list = {}
    chat_ai_bot_list = {}
    insult_bot_list = {}
    
    @staticmethod
    def getInstance():
        if bot_manager.__instance == None:
            bot_manager()
        return bot_manager.__instance
    
    def __init__(self):
        if bot_manager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            bot_manager.__instance = self
    

    def update_player_list(self, mc):
        newList = mc.getPlayerEntityIds()
        if len(newList) > len(self.player_list):
            diff = list(set(newList).difference(self.player_list))
            self.player_list.extend(diff)
            for player in diff:
                self.tnt_bot_list[player] = tnt(player)
                self.chat_ai_bot_list[player] = gpt(player)
                self.insult_bot_list[player] = Insult(player)
            self.printLists()
        
        elif len(newList) < len(self.player_list):
            diff = list(set(self.player_list).difference(newList))
            self.player_list = newList
            for player in diff:
                self.tnt_bot_list[player].stop()
                del self.tnt_bot_list[player]
                
                self.chat_ai_bot_list[player].stop()
                del self.chat_ai_bot_list[player]
                
                self.insult_bot_list[player].stop()
                del self.insult_bot_list[player]
            self.printLists()
            
   
    def get_bot_list(self, bot_type):     
        print(f"Received bot type: {bot_type}")
        switcher = {
            'TNT'.casefold(): self.tnt_bot_list,
            'ChatBOT'.casefold(): self.chat_ai_bot_list,
            'Insult'.casefold(): self.insult_bot_list
        }
        return switcher.get(bot_type.casefold(), None)

    
    
    def printLists(self):
        print("Player list = "+str(self.player_list))
        print("TNT list = "+str(self.tnt_bot_list))
        print("GPT list = "+str(self.chat_ai_bot_list))
        print("Insult list = "+str(self.insult_bot_list))
        