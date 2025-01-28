import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from botclass import Bot, BotManager, TNT, ChatAI, Insult



class TestBots(unittest.TestCase):
    
    def setUp(self):
        # Mockear la conexión a Minecraft
        self.mc_mock = MagicMock()
        self.player_mock = 12345

        # Mock para métodos de Minecraft
        self.mc_mock.entity.getName.return_value = "TestPlayer"
        self.mc_mock.getPlayerEntityIds.return_value = [self.player_mock]

    @patch('botclass.game.Minecraft.create')
    def test_tnt_bot_activation(self, mock_mc_create):
        mock_mc_create.return_value = self.mc_mock

        # Crear y activar el bot
        bot = TNT(self.player_mock)
        bot.begin()
        bot.mc.postToChat.assert_called_with("§2<TNTBot> ***The bot has been enabled for TestPlayer!!")

    @patch('botclass.game.Minecraft.create')
    def test_tnt_bot_stop(self, mock_mc_create):
        mock_mc_create.return_value = self.mc_mock

        # Crear y detener el bot
        bot = TNT(self.player_mock)
        bot.begin()
        bot.stop()
        bot.mc.postToChat.assert_called_with("§2<TNTBot> ***The bot has been disabled for TestPlayer!!")

    @patch('botclass.game.Minecraft.create')
    def test_bot_manager_add_player(self, mock_mc_create):
        mock_mc_create.return_value = self.mc_mock

        manager = BotManager.getInstance()
        manager.update_player_list(self.mc_mock)

        # Comprobar que el jugador fue agregado a la lista
        self.assertIn(self.player_mock, manager.player_list)


class TestBotManager(unittest.TestCase):

    @patch('botclass.game.Minecraft.create')
    def test_bot_manager_get_bot_list(self, mock_mc_create):
        mock_mc_create.return_value = MagicMock()
        manager = BotManager.getInstance()
        
        # Mockear listas de bots
        manager.tnt_bot_list = {123: TNT(123)}
        manager.chat_ai_bot_list = {123: ChatAI(123)}
        manager.insult_bot_list = {123: Insult(123)}
        
        # Probar la obtención de listas de bots
        self.assertIn(123, manager.get_bot_list('TNT'))
        self.assertIn(123, manager.get_bot_list('ChatAI'))
        self.assertIn(123, manager.get_bot_list('Insult'))


if __name__ == '__main__':
    unittest.main()