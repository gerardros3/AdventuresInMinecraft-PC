from read_chat import *
from baseBot import Bot, generate_response
from threading import Thread
from dotenv import dotenv_values


class InsultBOT(Bot):
    def __init__(self, entity):
        super().__init__(entity)
        self.name = "InsultBot"  # Name of the bot
        self.t1 = Thread(target=self._main)  # Update thread with the function to execute
        self.bot_entity_id = self.t1.name
        self.player_name = self.mc.entity.getName(self.entity)
        # HugChat setup
        try:
            secrets = dotenv_values('C:\\users\\stef2\\Desktop\\Minecraft-agent-framework\\MyAdventures\\hf.env')
            self.hf_email = secrets['EMAIL']
            self.hf_pass = secrets['PASS']
        except Exception as e:
            print(f"§2Error loading HugChat credentials: {e}")

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
                    self.insult_command("Generate low insults for this player: "+ self.player_name + "(Keep it short please), he typed this: "+text)


    # Function to handle GPT prompts
    def insult_command(self, prompt):
        try:
            response = generate_response(prompt, self.hf_email, self.hf_pass)
            self.mc.postToChat(f"<Insult> {response}")  # Limit response length
            #response.close();
        except Exception as e:
            self.mc.postToChat(f"<Insult> Error: {str(e)}")
            self.mc.postToChat(f"<Insult> Error: {str(e)}")