from framework.base_bot import Bot
from threading import Thread
import random


class Insult(Bot):
    def __init__(self, entity):
        super().__init__(entity)
        self.name = "InsultBot"  # Nombre del bot
        self.t1 = Thread(target=self._main)  # Crear el hilo que ejecutará la función principal
        self.bot_entity_id = self.t1.name  # ID del bot para evitar que se insulte a sí mismo
        self.player_name = self.mc.entity.getName(self.entity)  # Obtener el nombre del jugador que llamó al bot

        # Lista de insultos cargada en __init__ para no recargarla repetidamente
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



    # Función principal del bot Insult (para procesar comandos)
    def _main(self):
        while self.control:
            chatEvents = self.mc.events.pollChatPosts()  # Leer los eventos de chat
            
            for command in chatEvents:
                text = str(command.message)  # Convertir el mensaje del chat a cadena
                sender_entity_id = command.entityId  # Obtener el ID del jugador que envió el mensaje
                if sender_entity_id == self.bot_entity_id:
                    continue  # Evitar que el bot se insulte a sí mismo
                
                if not text.startswith(":") and not text.startswith("<"):  # Filtrar mensajes que no son comandos o interacciones
                    self.insult_command("Generar insultos para el jugador: " + self.player_name)  # Llamar a la función para generar un insulto

    # Función para generar un insulto
    def insult_command(self, prompt):
        try:
            # Elegir un insulto aleatorio
            insult = random.choice(self.insults)
            self.mc.postToChat(f"<InsultBot> {insult}")  # Enviar el insulto al chat
        except Exception as e:
            self.mc.postToChat(f"<InsultBot> Error: {str(e)}")  # En caso de error, enviar un mensaje de error al chat
