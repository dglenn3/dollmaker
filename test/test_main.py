import unittest.mock
import pygame as pg
import shutil
import tempfile
import os

import main

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        os.environ["IMAGE_DIR"] = tempfile.mkdtemp()
        self.image_dir = os.environ.get("IMAGE_DIR")

        with open(os.path.join(self.image_dir, 'test_image.png'), 'w') as f:
            f.write("test image data")

        # Create subdirectories and images in the test image directory
        for i in range(3):
            subdir_name = f"subdir_{i}"
            subdir_path = os.path.join(self.image_dir, subdir_name)
            os.mkdir(subdir_path)
            for j in range(2):
                image_name = f"image_{j}.png"
                image_path = os.path.join(subdir_path, image_name)
                with open(image_path, "w") as f:
                    f.write("test image data")

        pg.display.set_mode()

        self.surface = pg.Surface((1,1))
        pg.image.load = unittest.mock.Mock()
        pg.image.load.return_value = self.surface

    def tearDown(self):
        # Remove the test image directory and its contents
        shutil.rmtree(self.image_dir)

        # Unset the value of the IMAGE_DIR environment variable
        os.environ.pop("IMAGE_DIR")

class TestLoadComponent(BaseTestCase):
    def test_load_component(self):
        assert(main.load_component("test_image.png", self.image_dir).get("rect") == self.surface.get_rect())

    def test_load_component_with_directory(self):
        assert(main.load_component("image_0.png", self.image_dir, "subdir_0").get("rect") == self.surface.get_rect())

class TestLoadDynamicImages(BaseTestCase):
    def test_load_dynamic_components(self):
        components = main.load_dynamic_components(self.image_dir)
        assert(len(components) == 3)
        assert(len(components[1]) == 2)

    def test_load_dynamic_components_default_directory(self):
        components = main.load_dynamic_components()
        assert(len(components) == 3)
        assert(len(components[1]) == 2)

class TestStaticImages(BaseTestCase):
    def test_load_static_images(self):
        images = main.load_static_images()
        assert(len(images) == 1)


class TestLoadButtons(BaseTestCase):
    def test_load_all_buttons(self):
        components = main.load_dynamic_components(self.image_dir)
        all_buttons = main.load_all_buttons(components)
        assert(len(all_buttons) == 6)

if __name__ == '__main__':
    unittest.main()