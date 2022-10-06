import pygame as pg

class Button(pg.sprite.Sprite):
    """Creates a button that can be used to
    change an image"""

    def __init__(self, top, left, component):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pg.transform.smoothscale(component.get("image"), (50, 50))
        self.rect = pg.Rect(0, 0, 50, 50)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = (left + 1) * 100 + 300, (top + 1) * 75
        self.directory = top
        self.index = left
    
    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False
