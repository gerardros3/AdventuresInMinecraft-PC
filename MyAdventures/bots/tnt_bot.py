import random
import time
import mcpi.entity as entities
from threading import Thread
from framework.base_bot import Bot


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
