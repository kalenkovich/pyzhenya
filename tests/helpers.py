from __future__ import annotations

from pathlib import Path

from PIL import Image

# assert_image_equal and assert_image_equal_tofile were copied (with logging removed) from Pillow's Tests/helper.py:
# https://github.com/python-pillow/Pillow/blob/cb9e3535c4db91036210159424dcc71ea9fe0d6a/Tests/helper.py#L97


def assert_image_equal(a: Image.Image, b: Image.Image, msg: str | None = None) -> None:
    assert a.mode == b.mode, msg or f"got mode {repr(a.mode)}, expected {repr(b.mode)}"
    assert a.size == b.size, msg or f"got size {repr(a.size)}, expected {repr(b.size)}"
    assert a.tobytes() == b.tobytes(), msg or "got different content"


def assert_image_equal_tofile(
    a: Image.Image, filename: str, msg: str | None = None, mode: str | None = None
) -> None:
    with Image.open(filename) as img:
        if mode:
            img = img.convert(mode)
        assert_image_equal(a, img, msg)


def assert_image_files_equal(path1: str | Path, path2: str | Path) -> None:
    with Image.open(path1) as img1, Image.open(path2) as img2:
        assert_image_equal(img1, img2)
