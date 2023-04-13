import unittest.mock
import pygame as pg
import os

import main

class TestLoadComponent(unittest.TestCase):
    def test_load_component(self):
        pg.display.set_mode()
        surface = pg.Surface((1,1))
        pg.image.load = unittest.mock.Mock()
        pg.image.load.return_value = surface

        assert(main.load_component("base.png").get("rect") == surface.get_rect())

    def test_load_component_with_directory(self):
        pg.display.set_mode()
        surface = pg.Surface((1,1))
        pg.image.load = unittest.mock.Mock()
        pg.image.load.return_value = surface

        assert(main.load_component("femaleBlueEyes.png", "eyes").get("rect") == surface.get_rect())

class TestLoadDynamicImages(unittest.TestCase):
    def test_load_dynamic_components(self):
        pg.display.set_mode()
        surface = pg.Surface((1,1))
        pg.image.load = unittest.mock.Mock()
        pg.image.load.return_value = surface

        image_dir = os.path.join(os.path.split(os.path.abspath(__file__))[0], "images")

        components = main.load_dynamic_components(image_dir)
        assert(len(components) == 4)
        assert(len(components[1]) == 2)

    def test_load_dynamic_components_default_directory(self):
        pg.display.set_mode()
        surface = pg.Surface((1,1))
        pg.image.load = unittest.mock.Mock()
        pg.image.load.return_value = surface

        components = main.load_dynamic_components()
        assert(len(components) == 4)
        assert(len(components[1]) == 6)

class TestStaticImages(unittest.TestCase):
    def test_load_static_images(self):
        pg.display.set_mode()
        image_dir = os.path.join(os.path.split(os.path.abspath(__file__))[0], "images")

        images = main.load_static_images(image_dir)
        assert(len(images) == 1)


class TestLoadButtons(unittest.TestCase):
    def test_load_all_buttons(self):
        pg.display.set_mode()
        surface = pg.Surface((1,1))
        pg.image.load = unittest.mock.Mock()
        pg.image.load.return_value = surface

        image_dir = os.path.join(os.path.split(os.path.abspath(__file__))[0], "images")

        components = main.load_dynamic_components(image_dir)
        all_buttons = main.load_all_buttons(components)
        assert(len(all_buttons) == 7)

if __name__ == '__main__':
    unittest.main()