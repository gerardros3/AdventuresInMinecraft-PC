from mcpi.minecraft import Minecraft

class BaseBot:
    def __init__(self, name):
        self.mc = Minecraft.create()
        self.name = name
        self.posicion = self.mc.player.getTilePos()
        self.event_system = None
        

    def run(self):
        self.mc.postToChat(f"Hello {self.name}!")
        
    def get_block(self, x, y, z):
        return self.mc.getBlock(x, y, z)

    def set_block(self, x, y, z, block):
        self.mc.setBlock(x, y, z, block)
    
    def set_event_system(self, event_system, callBack):
        if self.event_system:
            self.event_system.register_event(event_system), callBack
        else:
            print("No event system found")
            
    @staticmethod
    def is_question(message):
        """
        Check if the message is a question
        :param message: string 
        :return
        """
        return message.endswith("?")
            
            