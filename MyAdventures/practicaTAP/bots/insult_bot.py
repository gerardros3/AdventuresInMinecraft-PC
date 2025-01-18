from mcpi.minecraft import Minecraft
import random
from framework.base_bot import BaseBot

mc = Minecraft.create()

class InsultBot(BaseBot):
    def __init__(self, mc):
        self.mc = mc
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

    def send_insult(self):
        insult = random.choice(self.insults)
        self.mc.postToChat(insult)

# Example usage
insult_bot = InsultBot(mc)
insult_bot.send_insult()