import typing as t

from PIL import Image, ImageDraw, ImageFont


def create_images_grid_by_columns(
    images: t.List[Image.Image],
    gap: int,
    max_columns: int,
) -> Image.Image:
    max_rows = (len(images) + max_columns - 1) // max_columns
    return _create_images_grid(images=images, gap=gap, max_columns=max_columns, max_rows=max_rows)


def create_images_grid_by_rows(
    images: t.List[Image.Image],
    gap: int,
    max_rows: int,
) -> Image.Image:
    max_columns = (len(images) + max_rows - 1) // max_rows
    return _create_images_grid(images=images, gap=gap, max_columns=max_columns, max_rows=max_rows)


def _create_images_grid(
    images: t.List[Image.Image],
    gap: int,
    max_columns: int,
    max_rows: int,
) -> Image.Image:
    size = images[0].size

    grid_width = size[0] * max_columns + (max_columns - 1) * gap
    grid_height = size[1] * max_rows + (max_rows - 1) * gap

    grid_image = Image.new("RGB", (grid_width, grid_height), color="white")

    for i, image in enumerate(images):
        image = image.crop((0, 0, size[0], size[1]))
        x = (i % max_columns) * (size[0] + gap)
        y = (i // max_columns) * (size[1] + gap)

        grid_image.paste(image, (x, y))

    return grid_image


def _draw_center_text(
  text: str,
  draw: ImageDraw.ImageDraw,
  font: ImageFont.ImageFont,
  fill: int = 128,
):
  image = draw.im  # type: ignore
  _, _, *text_size = draw.textbbox((0, 0), text, font=font)
  draw.text(
    (
      (image.size[0]-text_size[0])/2,
      (image.size[1]-text_size[1])/2,
    ),
    text,
    font=font,
    fill=fill,
  )
  return image
