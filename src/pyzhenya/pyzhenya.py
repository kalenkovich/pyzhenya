from __future__ import annotations

from pathlib import Path
from typing import Union

from PIL import Image, ImageDraw, ImageFont


def text_to_image(text: str) -> Image.Image:
    """Creates a PIL image object with the given text.

    The image will have transparent background and minimal padding and will be in the "RGBA" mode.

    Parameters
    ----------
    text : str
        The text to convert into an image

    Returns
    -------
    Image.Image
        The image object

    Examples
    --------
    >>> from pyzhenya.pyzhenya import text_to_image
    >>> image = text_to_image("😍")
    >>> image.show()
    """
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
    """Creates an image file with the given text.

    The image will have transparent background and minimal padding. The output format will be inferred by PIL from
    the output file name.

    Parameters
    ----------
    text : str
        The text to convert into an image
    output_path : str | Path
        The output path for the image file

    Returns
    -------
    None

    Examples
    --------
    >>> from pyzhenya.pyzhenya import text_to_image_file
    >>> text_to_image_file("😍", "heart-eyes.png")
    """
    text_to_image(text).save(output_path)
