import unittest.mock
import pygame as pg
from dynamicimage import DynamicImage

class TestDynamicImage(unittest.TestCase):
    def test_change_image(self):
        surface = pg.Surface((1,1))
        new_surface = pg.Surface((2,2))

        pg.display.set_mode()
        component = {"image": surface, "rect": surface.get_rect()}
        new_component = {"image": new_surface, "rect": new_surface.get_rect()}
        base = DynamicImage(component)
        base.change_image(new_component)
        assert(base.image == new_surface)
        assert(base.rect == new_surface.get_rect())
