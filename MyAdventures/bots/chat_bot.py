from read_chat import *
from baseBot import Bot, generate_response
from threading import Thread
from dotenv import dotenv_values

# Main ChatAI Bot Class
class ChatBOT(Bot):
    def __init__(self, entity):
        super().__init__(entity)
        self.name = "ChatBot"  # Name of the bot
        self.t1 = Thread(target=self._main)  # Update thread with the function to execute
        # HugChat setup
        try:
            secrets = dotenv_values('C:\\users\\stef2\\Desktop\\Minecraft-agent-framework\\MyAdventures\\hf.env')
            self.hf_email = secrets['EMAIL']
            self.hf_pass = secrets['PASS']
        except Exception as e:
            print(f"§2Error loading HugChat credentials: {e}")

    # Main function for the ChatAI bot (to process commands)
    def _main(self):
        while self.control:
            chatEvents = self.mc.events.pollChatPosts()
    
            for command in chatEvents:
                text = str(command.message) # Convert chat event to str
                if(not text.startswith(":gpt ")):   # Skip if it doesn't start with ":gpt"
                    continue
                else:
                    text = text[4:]
                    self.handle_gpt_command(text + "  ")

    # Function to handle GPT prompts
    def handle_gpt_command(self, prompt):
        try:
            response = generate_response(prompt, self.hf_email, self.hf_pass)
            self.mc.postToChat(f"<GPT> {response}")  # Limit response length
            #response.close();
        except Exception as e:
            self.mc.postToChat(f"<GPT> Error: {str(e)}")