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
            "You're about as sharp as a marble.",
            "I've met goldfish with better memories.",
            "You bring balance to the universe... by lowering the average IQ.",
            "Beauty fades, but stupidity is forever — lucky you!",
            "I'd agree with you, but I have a thing against being wrong.",
            "You bring a whole new meaning to 'thinking outside the box' — because there's no box, just emptiness.",
            "You're not even good at being bad at things.",
            "If cluelessness were a sport, you'd be an Olympic champion.",
            "You're so lost, even GPS can't find your common sense.",
            "You're not the dumbest person I've met, but you're running a close second.",
            "You're so technologically challenged, you'd try to fax a pizza.",
            "You're about as reliable as a paper umbrella in a hurricane.",
            "You're the kind of person who claps when the plane lands.",
            "You're proof that even mistakes can be persistent.",
            "You're so creative — no one else would have thought of that nonsense."
        ]


            insult = random.choice(self.insults)
            self.mc.postToChat(f"<InsultBot> {insult}")
        except Exception as e:
            self.mc.postToChat(f"<InsultBot> Error: {str(e)}")