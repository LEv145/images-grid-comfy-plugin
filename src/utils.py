import typing as t

import torch
import numpy as np
from PIL import Image


def tensor_to_pillow(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def pillow_to_tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


def create_image_grid_by_columns(
    images: t.List[Image.Image],
    gap: int,
    max_columns: int,
) -> Image.Image:
    max_rows = (len(images) + max_columns - 1) // max_columns
    return create_image_grid(images=images, gap=gap, max_columns=max_columns, max_rows=max_rows)


def create_image_grid_by_rows(
    images: t.List[Image.Image],
    gap: int,
    max_rows: int,
) -> Image.Image:
    max_columns = (len(images) + max_rows - 1) // max_rows
    return create_image_grid(images=images, gap=gap, max_columns=max_columns, max_rows=max_rows)


def create_image_grid(
    images: t.List[Image.Image],
    gap: int,
    max_columns: int,
    max_rows: int,
) -> Image.Image:
    size = images[0].size

    width = size[0] * max_columns + (max_columns - 1) * gap
    height = size[1] * max_rows + (max_rows - 1) * gap

    grid_image = Image.new("RGB", (width, height), color="white")

    for i, image in enumerate(images):
        x = (i % max_columns) * (size[0] + gap)
        y = (i // max_columns) * (size[1] + gap)

        grid_image.paste(image, (x, y))

    return grid_image
