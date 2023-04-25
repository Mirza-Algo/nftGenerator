import os
import random
import json
from string import ascii_letters
from typing import List
from PIL import Image, ImageDraw, ImageFont
from layer import Layer
import textwrap


class AvatarGenerator:
    def __init__(self, images_path: str):
        self.layers: List[Layer] = self.load_image_layers(images_path)
        self.background_color = (120, 150, 180)
        self.rare_background_color = (255, 225, 150)
        self.rare_background_chance = 0.05
        self.output_path: str = "./output"
        os.makedirs(self.output_path, exist_ok=True)

    def load_image_layers(self, images_path: str):
        sub_paths = sorted(os.listdir(images_path))
        layers: List[Layer] = []
        for sub_path in sub_paths:
            layer_path = os.path.join(images_path, sub_path)
            layer = Layer(layer_path)
            layers.append(layer)

        """ layers[0].rarity = 0.50
        layers[1].rarity = 0.50 """

        return layers

    def generate_image_sequence(self):
        image_path_sequence = []
        for layer in self.layers:
            if layer.should_generate():
                image_path = layer.get_random_image_path()
                image_path_sequence.append(image_path)
        print(image_path_sequence)
        return image_path_sequence

    def render_avatar_image(self, image_path_sequence: List[str], book):

        if random.random() < self.rare_background_chance:
            bg_color = self.rare_background_color
        else:
            bg_color = self.background_color

        # image = Image.new("RGBA", (3000, 4500), bg_color)
        for layer in self.layers:
            fontPath = layer.get_random_font_path()
            basePath = layer.get_random_base_path()
            basePath2 = layer.get_random_base_path_2()

        image = Image.open(basePath).convert("RGBA")
        layer_image = Image.open(image_path_sequence[1]).convert("RGBA")
        #3rd layer
        image2 = Image.open(basePath2).convert("RGBA")
        image_raw = Image.alpha_composite(image, image2)
        image = Image.alpha_composite(image_raw, layer_image)
        draw = ImageDraw.Draw(image)
        # print(book)
        # Load custom font
        book_title_font = ImageFont.truetype(fontPath, size=320)
        author_name_font = ImageFont.truetype(fontPath, size=100)
        # Create DrawText object
        draw = ImageDraw.Draw(im=image)

        # Calculate the average length of a single character of our font.
        # Note: this takes into account the specific font and font size.
        avg_char_width = sum(book_title_font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
        # Translate this average length into a character count
        max_char_count = int(image.size[0] * .700 / avg_char_width)

        avg_char_width_author = sum(author_name_font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
        # Translate this average length into a character count
        max_char_count_author = int(image.size[0] * .700 / avg_char_width_author)
        # Create a wrapped text object using scaled character count
        book_title = textwrap.fill(text=book['book_title'], width=max_char_count)
        author_name = textwrap.fill(text=book['author_name'], width=max_char_count_author)
        # Add text to the image
        draw.text(xy=(image.size[0]/2, 1200), text=book_title, font=book_title_font, anchor='mm', align='center', fill="#FFFFFF")
        draw.text(xy=(image.size[0]/2, 3500), text=author_name, font=author_name_font, anchor='mm', align='center', fill="#FFFFFF")
        
        return image

    def save_image(self, image: Image.Image, i: int = 0):
        image_index = str(i).zfill(4)
        image_file_name = f"{image_index}.png"
        image_save_path = os.path.join(self.output_path, image_file_name)
        image.save(image_save_path)

    def generate_avatar(self, n: int = 1):
        print("COMN: Generating NFTs, please wait. it may take a while... \nPress Ctrl+C to abort\n.\n.")
        json_file = open('IndiaFiction.json')
        titlesFromJson = json.load(json_file)
        for i in titlesFromJson['BookNFTs']:
            image_path_sequence = self.generate_image_sequence()
            image = self.render_avatar_image(image_path_sequence, i)
            self.save_image(image, i['book_title'])
