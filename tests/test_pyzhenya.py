import pytest
from pyzhenya.pyzhenya import text_to_image, text_to_image_file

from .helpers import assert_image_equal_tofile, assert_image_files_equal


@pytest.fixture
def heart_eyes_emoji():
    return "😍"


@pytest.fixture
def heart_eyes_png_path():
    return "tests/heart-eyes.png"


def test_text_to_image(heart_eyes_emoji, heart_eyes_png_path):
    image = text_to_image(heart_eyes_emoji)
    assert image.mode == "RGBA"
    assert image.size == (247, 248)
    assert_image_equal_tofile(image, heart_eyes_png_path)


def test_text_to_image_file(tmp_path, heart_eyes_emoji, heart_eyes_png_path):
    output_image_path = tmp_path / "heart-eyes.png"
    text_to_image_file(heart_eyes_emoji, output_image_path)
    assert output_image_path.exists()
    assert_image_files_equal(output_image_path, heart_eyes_png_path)
