import unittest.mock
import pygame as pg

import main

class TestLoadImage(unittest.TestCase):
    def test_load_image(self):
        pg.display.set_mode((900, 650), pg.SCALED)
        surface = pg.Surface((1,1))
        pg.image.load = unittest.mock.Mock()
        pg.image.load.return_value = surface

        assert(main.load_image("base.png") == surface, surface.get_rect())

class TestImage(unittest.TestCase):
    def test_change_image_no_change(self):
        pg.display.set_mode((900, 650), pg.SCALED)
        base = main.Image("base.png", 1, None, 1)
        assert(base.index == 0)
        base.change_image()
        # index does not increment when length is 1
        assert(base.index == 0)

    def test_change_image_cycle_through_all(self):
        pg.display.set_mode((900, 650), pg.SCALED)
        base = main.Image("base.png", 3, None, 1)
        base.change_image()
        assert(base.index == 1)
        base.change_image()
        assert(base.index == 2)
        base.change_image()
        assert(base.index == 0)

class TestButton(unittest.TestCase):
    def test_check_click_no_collision(self):
        pg.display.set_mode((900, 650), pg.SCALED)
        button1 = main.Button(1)
        assert(button1.check_click((0,0)) == False)

    def test_check_click_with_collision(self):
        pg.display.set_mode((900, 650), pg.SCALED)
        button1 = main.Button(1)
        assert(button1.check_click((500,150)) == True)

class TestLoadAllImages(unittest.TestCase):
    def test_load_all_image(self):
        pg.display.set_mode((900, 650), pg.SCALED)
        surface = pg.Surface((1,1))
        pg.image.load = unittest.mock.Mock()
        pg.image.load.return_value = surface

        assert(main.load_all_images() == surface, surface.get_rect())


if __name__ == '__main__':
    unittest.main()