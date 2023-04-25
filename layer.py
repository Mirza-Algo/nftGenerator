import os
import random


class Layer:
    def __init__(self, path: str):
        self.path = path
        self.rarity: float = 1.0

    def get_random_image_path(self):
        image_file_names = os.listdir(self.path)
        random_image_file_name = random.choice(image_file_names)
        return os.path.join(self.path, random_image_file_name)

    def should_generate(self) -> bool:
        return random.random() < self.rarity
    
    def get_random_font_path(self):
        font_file_names = os.listdir('./fonts')
        random_font_file_name = random.choice(font_file_names)
        return os.path.join('./fonts', random_font_file_name)
    
    def get_random_base_path(self):
        base_file_name = os.listdir('./images/0_bg')
        random_base_file_name = random.choice(base_file_name)
        return os.path.join('./images/0_bg', random_base_file_name)
    
    def get_random_base_path_2(self):
        base_file_name = os.listdir('./images/2_img')
        random_base_file_name = random.choice(base_file_name)
        return os.path.join('./images/2_img', random_base_file_name)
