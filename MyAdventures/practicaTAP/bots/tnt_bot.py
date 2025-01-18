from mcpi.minecraft import Minecraft
from mcpi import block
import time
from framework.base_bot import BaseBot

mc = Minecraft.create()

class TNTBot(BaseBot):
    def __init__(self, mc):
        self.mc = mc

    def place_tnt(self, x, y, z):
        self.mc.setBlock(x, y, z, block.TNT.id, 1)  # Place TNT block
        time.sleep(2)
        self.mc.setBlock(x, y, z, block.AIR.id)  # Ignite TNT

# Example usage
tnt_bot = TNTBot(mc)
tnt_bot.place_tnt(10, 10, 10)