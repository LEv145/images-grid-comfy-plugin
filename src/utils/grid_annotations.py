import typing as t
from dataclasses import dataclass

from PIL import Image, ImageDraw, ImageFont


@dataclass
class GridImagesInfo():
    image: Image.Image
    gap: int
    one_image_size: t.Tuple[int, int]


def create_grid_annotations(
    grid_info: GridImagesInfo,
    column_texts,
    row_texts,
    font: ImageFont.ImageFont,
    margin: int = 5,
) -> Image.Image:
    grid = grid_info.image
    left_padding = int(max(map(font.getlength, row_texts))) + 2*margin  # type: ignore
    top_padding = font.size + 2*margin  # type: ignore

    image = Image.new(
        "RGB",
        (grid.size[0] + left_padding, grid.size[1] + top_padding),
        color="white",
    )
    draw = ImageDraw.Draw(image)
    draw.font = font  # type: ignore

    image.paste(grid, (image.size[0] - grid.size[0], image.size[1] - grid.size[1]))
    _draw_column_text(
        draw=draw,
        texts=column_texts,
        grid_info=grid_info,
        left_padding=left_padding,
        top_padding=top_padding,
    )
    _draw_row_text(
        draw=draw,
        texts=row_texts,
        grid_info=grid_info,
        left_padding=left_padding,
        top_padding=top_padding,
    )

    return image


def _draw_column_text(
    draw: ImageDraw.ImageDraw,
    texts: t.List[str],
    grid_info: GridImagesInfo,
    left_padding: int,
    top_padding: int,
) -> None:
    i = 0
    x0 = left_padding
    y0 = 0
    x1 = left_padding + grid_info.one_image_size[0]
    y1 = top_padding
    while x0 != grid_info.image.size[0] + left_padding:
        _draw_center_text(draw, (x0, y0, x1, y1), texts[i])
        x0 += grid_info.one_image_size[0] + grid_info.gap
        x1 += grid_info.one_image_size[0] + grid_info.gap
        i += 1


def _draw_row_text(
    draw: ImageDraw.ImageDraw,
    texts: t.List[str],
    grid_info: GridImagesInfo,
    left_padding: int,
    top_padding: int,
) -> None:
    i = 0
    x0 = 0
    y0 = top_padding
    x1 = left_padding
    y1 = top_padding + grid_info.one_image_size[1]
    while y0 != grid_info.image.size[1] + top_padding:
        _draw_center_text(draw, (x0, y0, x1, y1), texts[i])
        y0 += grid_info.one_image_size[1] + grid_info.gap
        y1 += grid_info.one_image_size[1] + grid_info.gap
        i += 1


def _draw_center_text(
    draw: ImageDraw.ImageDraw,
    xy: t.Tuple[int, int, int, int],
    text: str,
    fill: t.Any = "black",
) -> None:
    _, _, *text_size = draw.textbbox((0, 0), text)
    draw.text(
        (
            (xy[2] - text_size[0] + xy[0]) / 2,
            (xy[3] - text_size[1] + xy[1]) / 2,
        ),
        text,
        fill=fill,
    )
