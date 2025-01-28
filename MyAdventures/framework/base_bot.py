import mcpi.minecraft as game
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
        