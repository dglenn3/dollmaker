#!/usr/bin/env python
""" pygame.examples.chimp

This simple application allows you to 
use your own art to create a doll maker. 
"""


# Import Modules
import os
import pygame as pg

if not pg.font:
    print("Warning, fonts disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "images")
length = 3


# functions to create our resources
def load_image(name, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)
    image = image.convert_alpha()

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)
    return image, image.get_rect()


# def load_all_images():
#     dirs = os.listdir(data_dir)
#     for name in dirs:
#         print(name)


# classes for our game objects
class Image(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("base.png")
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 5, 5
        self.index = 0

    def update(self):
        """Update the image based on the user selection"""
        if self.index == 0:
            self.image, self.rect = load_image("base.png")
        else:
            self.image, self.rect = load_image(f"test{self.index + 1}.png")
        self.rect.topleft = 5, 5

    def change_image(self, target):
        """Cycle to the next image in the sequence"""
        if self.index < length - 1:
            self.index += 1
        else:
            self.index = 0

class Cursor(pg.sprite.Sprite):
    """The in-game cursor, following the mouse"""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("cursor.png", 0.25)

    def update(self):
        """Move the cursor based on the mouse position"""
        pos = pg.mouse.get_pos()
        self.rect.topleft = pos

class Button(pg.sprite.Sprite):
    """Creates a button that can be used to
    cycle through the list of images"""

    def __init__(self, topleft):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("danger.gif")
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 500, topleft * 150

def main():
    """this function is called when the program starts.
    it initializes everything it needs, then runs in
    a loop until the function returns."""
    # Initialize Everything
    pg.init()

    screen = pg.display.set_mode((900, 650), pg.SCALED)
    # Create The Background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    # Put Text On The Background, Centered
    if pg.font:
        font = pg.font.Font(None, 64)
        text = font.render("Wave the aqua rod on danger to change image", True, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        background.blit(text, textpos)

    # Display The Background
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Prepare Game Objects
    image = Image()
    button = Button(1)
    button2 = Button(2)
    button_list = [button, button2]
    cursor = Cursor()
    allsprites = pg.sprite.RenderPlain((image, button, cursor))
    # load_all_images()

    # Main Loop
    going = True
    while going:

        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                clicked = pg.sprite.spritecollide(cursor, button_list, False)
                if len(clicked) > 0:
                    image.change_image(clicked)

        allsprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pg.display.flip()

    pg.quit()


# Game Over


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
