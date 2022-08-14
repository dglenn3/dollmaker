#!/usr/bin/env python
""" 
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


# functions to create our resources
def load_image(name, type=None, scale=1):
    if(type):
        fullname = os.path.join(data_dir, type, name)
    else:
        fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)
    image = image.convert_alpha()

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)
    return image, image.get_rect()

# classes for our game objects
class Image(pg.sprite.Sprite):

    def __init__(self, name, length=0, type=None, scale=1):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image(name, type, scale)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 5, 5
        self.index = 0
        self.length = length
        self.type = type

    def update(self):
        """Update the image based on the user selection"""
        self.image, self.rect = load_image(f"test{self.index + 1}.png", self.type, 1)
        self.rect.topleft = 5, 5

    def change_image(self):
        """Cycle to the next image in the sequence"""
        if self.index < self.length - 1:
            self.index += 1
        else:
            self.index = 0

class Button(pg.sprite.Sprite):
    """Creates a button that can be used to
    cycle through the list of images"""

    def __init__(self, topleft):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("danger.gif")
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 500, topleft * 150
    
    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

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
    background.fill((255, 255, 255))

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
    static = pg.sprite.Group()
    base = Image("base.png")
    static.add(base)
    animal = Image("test1.png", len(os.listdir(os.path.join(data_dir, "animals"))), "animals", 1)
    boot = Image("test1.png", len(os.listdir(os.path.join(data_dir, "boots"))), "boots", 1)
    image_list = [animal, boot]
    button1 = Button(1)
    button2 = Button(2)
    button_list = [button1, button2]
    static.draw(background)
    allsprites = pg.sprite.RenderPlain((animal, boot, button1, button2))

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
                for button in button_list:
                    if button.check_click(event.pos):
                        image_list[button_list.index(button)].change_image()

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
