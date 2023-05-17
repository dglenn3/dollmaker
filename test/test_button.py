import unittest.mock
import pygame as pg

import main
class TestButton(unittest.TestCase):
    def setUp(self):
        pg.display.set_mode((800, 600), pg.SCALED)
        surface = pg.Surface((300, 200))
        component = {"image": surface, "rect": surface.get_rect()}
        self.button = main.Button(1, 1, 100, component)
       
    def test_validate_and_update_position_within_window(self):
        initial_top, initial_left = 1, 1
        updated_top, updated_left = self.button.validate_and_update_position(100, initial_top, initial_left)
        
        assert(initial_top == updated_top)
        assert(initial_left == updated_left)

    def test_validate_and_update_position_outside_window(self):
        initial_top, initial_left = 1, 10
        updated_top, updated_left = self.button.validate_and_update_position(100, initial_top, initial_left)
        
        assert(updated_top == 2)
        assert(updated_left == 0)

    def test_check_click_no_collision(self):
        assert(self.button.check_click((0,0)) == False)

    def test_check_click_with_collision(self):
        assert(self.button.check_click((225, 125)) == True)