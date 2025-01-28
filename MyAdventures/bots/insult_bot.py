from framework.base_bot import Bot
from threading import Thread
import random



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