import unittest.mock
import pygame as pg

import main
class TestButton(unittest.TestCase):
    def test_check_click_no_collision(self):
        pg.display.set_mode()
        surface = pg.Surface((800, 600))
        component = {"image": surface, "rect": surface.get_rect()}
        button = main.Button(1,1,component)
        assert(button.check_click((0,0)) == False)

    def test_check_click_with_collision(self):
        pg.display.set_mode()
        surface = pg.Surface((800, 600))
        component = {"image": surface, "rect": surface.get_rect()}
        button = main.Button(1,1,component)
        assert(button.check_click((500,150)) == True)