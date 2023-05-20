import pygame as pg

class Button(pg.sprite.Sprite):
    """Creates a button that can be used to
    display an image"""

    def __init__(self, directory, index, left_offset, component):
        top, left = self.validate_and_update_position(left_offset, directory, index)
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pg.transform.smoothscale(component.get("image"), (50, 50))
        self.rect = pg.Rect(0, 0, 50, 50)
        self.rect.topleft = left * 75 + left_offset + 25, top * 75 + 25
        self.directory = directory
        self.index = index

    def validate_and_update_position(self, left_offset, top, left):
        window_width = pg.display.get_surface().get_size()[0]
        if(window_width - left_offset - (left * 75)) >= 0:
            return top, left
        left = left - 1 - (window_width - left_offset) // 75
        top += 1
        return self.validate_and_update_position(left_offset, top, left)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False
