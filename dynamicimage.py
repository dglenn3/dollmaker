import pygame as pg

class DynamicImage(pg.sprite.Sprite):

    def __init__(self, component):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = component.get("image") 
        self.rect = component.get("rect")

    def change_image(self, component):
        """Change to the image with the selected index"""
        self.image = component.get("image") 
        self.rect = component.get("rect")