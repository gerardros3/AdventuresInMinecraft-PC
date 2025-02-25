import unittest
from unittest.mock import patch, MagicMock
from framework.bot_manager import bot_manager as BotManager
from bots.tnt_bot import TNT
from bots.chat_bot import ChatBOT
from bots.insult_bot import Insult

class TestBots(unittest.TestCase):
    
    def setUp(self):
        # Mockear la conexión a Minecraft
        self.mc_mock = MagicMock()
        self.player_mock = 12345

        # Mock para métodos de Minecraft
        self.mc_mock.entity.getName.return_value = "TestPlayer"
        self.mc_mock.getPlayerEntityIds.return_value = [self.player_mock]

    @patch('framework.base_bot.game.Minecraft.create')
    def test_tnt_bot_activation(self, mock_mc_create):
        mock_mc_create.return_value = self.mc_mock

        # Crear y activar el bot
        bot = TNT(self.player_mock)
        bot.begin()
        bot.mc.postToChat.assert_called_with("§2<TNTBot> El bot ha sido habilitado para TestPlayer!")
        bot.stop()

    @patch('framework.base_bot.game.Minecraft.create')
    def test_tnt_bot_stop(self, mock_mc_create):
        mock_mc_create.return_value = self.mc_mock

        # Crear y detener el bot
        bot = TNT(self.player_mock)
        bot.begin()
        bot.stop()
        bot.mc.postToChat.assert_called_with("§2<TNTBot> El bot ha sido deshabilitado para TestPlayer!")

    @patch('framework.base_bot.game.Minecraft.create')
    def test_ChatBOT_bot_activation(self, mock_mc_create):
        mock_mc_create.return_value = self.mc_mock

        # Crear y activar el bot
        bot = ChatBOT(self.player_mock)
        bot.begin()
        bot.mc.postToChat.assert_called_with("§2<ChatBOT> El bot ha sido habilitado para TestPlayer!")
        bot.stop()

    @patch('framework.base_bot.game.Minecraft.create')
    def test_ChatBOT_bot_stop(self, mock_mc_create):
        mock_mc_create.return_value = self.mc_mock

        # Crear y detener el bot
        bot = ChatBOT(self.player_mock)
        bot.begin()
        bot.stop()
        bot.mc.postToChat.assert_called_with("§2<ChatBOT> El bot ha sido deshabilitado para TestPlayer!")

    @patch('framework.base_bot.game.Minecraft.create')
    def test_insult_bot_activation(self, mock_mc_create):
        mock_mc_create.return_value = self.mc_mock

        # Crear y activar el bot
        bot = Insult(self.player_mock)
        bot.begin()
        bot.mc.postToChat.assert_called_with("§2<InsultBot> El bot ha sido habilitado para TestPlayer!")
        bot.stop()

    @patch('framework.base_bot.game.Minecraft.create')
    def test_insult_bot_stop(self, mock_mc_create):
        mock_mc_create.return_value = self.mc_mock

        # Crear y detener el bot
        bot = Insult(self.player_mock)
        bot.begin()
        bot.stop()
        bot.mc.postToChat.assert_called_with("§2<InsultBot> El bot ha sido deshabilitado para TestPlayer!")

    @patch('framework.base_bot.game.Minecraft.create')
    def test_bot_manager_add_player(self, mock_mc_create):
        mock_mc_create.return_value = self.mc_mock

        manager = BotManager.getInstance()
        manager.update_player_list(self.mc_mock)

        # Comprobar que el jugador fue agregado a la lista
        self.assertIn(self.player_mock, manager.player_list)

class TestBotManager(unittest.TestCase):

    @patch('framework.base_bot.game.Minecraft.create')
    def test_bot_manager_get_bot_list(self, mock_mc_create):
        mock_mc_create.return_value = MagicMock()
        manager = BotManager.getInstance()
        
        # Mockear listas de bots
        manager.tnt_bot_list = {123: TNT(123)}
        manager.chat_ai_bot_list = {123: ChatBOT(123)}
        manager.insult_bot_list = {123: Insult(123)}
        
        # Probar la obtención de listas de bots
        self.assertIn(123, manager.get_bot_list('TNT'))
        self.assertIn(123, manager.get_bot_list('ChatBOT'))
        self.assertIn(123, manager.get_bot_list('Insult'))

if __name__ == '__main__':
    unittest.main()