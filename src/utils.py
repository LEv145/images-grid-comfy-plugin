import typing as t

import torch
import numpy as np
from PIL import Image


def tensor_to_pillow(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def pillow_to_tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


def create_image_grid(images: t.List[Image.Image], gap: int, ncol: int):
    # Calculate the number of rows needed based on the number of images and columns
    nrow = (len(images) + ncol - 1) // ncol

    # Get the size of the first image to use as a template for the grid
    size = images[0].size

    # Calculate the total size of the grid with gaps
    width = size[0] * ncol + gap * (ncol - 1)
    height = size[1] * nrow + gap * (nrow - 1)

    # Create a new image for the grid
    grid_image = Image.new("RGB", (width, height), color="white")

    # Iterate over each image and paste it into the grid
    for i, image in enumerate(images):
        # Calculate the position of the image in the grid
        x = (i % ncol) * (size[0] + gap)
        y = (i // ncol) * (size[1] + gap)

        # Paste the image into the grid
        grid_image.paste(image, (x, y))

    return grid_image
