# import unittest.mock
# import pygame as pg
# from dynamicimage import DynamicImage

# import main

# class TestDynamicImage(unittest.TestCase):
#     def test_change_image_no_change(self):
#         surface = pg.Surface((1,1))
#         pg.image.load = unittest.mock.Mock()
#         pg.image.load.return_value = surface

#         pg.display.set_mode()
#         base = DynamicImage("base.png", 1, None, 1)
#         base.change_image()
#         # index does not increment when length is 1
#         assert(base.index == 0)

#     def test_change_image_cycle_through_all(self):
#         pg.display.set_mode()
#         base = DynamicImage("base.png", 3, None, 1)
#         base.change_image()
#         assert(base.index == 1)
#         base.change_image()
#         assert(base.index == 2)
#         base.change_image()
#         assert(base.index == 0)