#!/usr/bin/env python
""" 
This simple application allows you to 
use your own art to create a doll maker. 
"""

# Import Modules
import os
import pygame as pg

from button import Button
from dynamicimage import DynamicImage

if not pg.font:
    print("Warning, fonts disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
image_dir = os.path.join(main_dir, "images")
dynamic_components = None

# functions to create our resources
def load_component(name, directory=None, scale=1):
    if(directory):
        fullname = os.path.join(image_dir, directory, name)
    else:
        fullname = os.path.join(image_dir, name)
    image = pg.image.load(fullname)
    image = image.convert_alpha()

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)
    return {"image": image, "rect": image.get_rect()}

def load_static_images():
    images = []
    for file_name in next(os.walk(image_dir))[2]:
        image = StaticImage(load_component(file_name))
        images.append(image)
    return images

def load_dynamic_components():
    components = []
    for directory_name in next(os.walk(image_dir))[1]:
        images = []
        for image_name in next(os.walk(os.path.join(image_dir, directory_name)))[2]:
            i = load_component(image_name, directory_name)
            images.append({"image": i.get("image"), "rect": i.get("rect")})
        components.append(images)
    return components

def load_all_buttons(dynamic_components):
    all_buttons = []
    for directory_index, directory in enumerate(dynamic_components):
        for component_index, component in enumerate(directory):
            button = Button(directory_index, component_index, component)
            all_buttons.append(button)
    return all_buttons

# classes for our game objects
class StaticImage(pg.sprite.Sprite):
    def __init__(self, component):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = component.get("image") 
        self.rect = component.get("rect")

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

    # Display The Background
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Prepare Game Objects
    static = pg.sprite.Group()
    static_images = load_static_images()
    static.add(static_images)
    global dynamic_components 
    dynamic_components = load_dynamic_components()
    all_buttons = load_all_buttons(dynamic_components)
    images_to_render = []
    for directory_index, directory in enumerate(dynamic_components):
        if(len(directory) > 0):
            images_to_render.append(DynamicImage(dynamic_components[directory_index][0]))
    static.draw(background)
    all_sprites = pg.sprite.RenderPlain((images_to_render, all_buttons))

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
                for button in all_buttons:
                    if button.check_click(event.pos):
                        images_to_render[button.directory].change_image(dynamic_components[button.directory][button.index])
                        break 

        all_sprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pg.display.flip()

    pg.quit()

# Game Over

# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
