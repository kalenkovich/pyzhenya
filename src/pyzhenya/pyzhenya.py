from __future__ import annotations

from pathlib import Path
from typing import Union

from PIL import Image, ImageDraw, ImageFont


def text_to_image(text: str) -> Image.Image:
    """Creates a PIL image object with the given text, transparent background, and minimal padding."""
    font = ImageFont.truetype('seguiemj.ttf', size=250, encoding='unic')
    (left, top, right, bottom) = font.getbbox(text)
    text_width = right - left
    text_height = bottom - top

    image = Image.new('RGBA', (text_width, text_height))
    draw = ImageDraw.Draw(image)
    draw.text((-left, -top), text, font=font, embedded_color=True)

    # crop the transparent edges (from https://gist.github.com/odyniec/3470977)
    image = image.crop(image.getbbox())

    return image


def text_to_image_file(text: str, output_path: Union[str | Path]) -> None:
    """Creates an image file with the given text, transparent background, and minimal padding."""
    text_to_image(text).save(output_path)
