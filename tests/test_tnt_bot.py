import unittest
from MyAdventures.practicaTAP.bots import TNTBot
from MyAdventures.mcpi import block

class TestTNTBot(unittest.TestCase):    
    def setUp(self):
        self.tnt_bot = TNTBot()

    def test_deploy_tnt(self):
        initial_pos = self.tnt_bot.get_position()
        self.tnt_bot.deploy_tnt()
        tnt_pos = (initial_pos.x + 1, initial_pos.y, initial_pos.z)
        block_type = self.tnt_bot.mc.getBlock(tnt_pos[0], tnt_pos[1], tnt_pos[2])
        self.assertEqual(block_type, block.TNT.id, "TNT block was not deployed correctly")
        
if __name__ == '__main__':
    unittest.main()