import typing as t

import torch
import numpy as np
from PIL import Image


def tensor_to_pillow(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def pillow_to_tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


def create_image_grid(images, gap, nrow):
    """
    Create a grid of images with a specified gap and number of rows.

    Args:
        images (List[PIL.Image.Image]): List of images to be placed in the grid.
        gap (int, optional): Gap between images in pixels. Defaults to 10.
        nrow (int, optional): Number of rows in the grid. Defaults to 3.

    Returns:
        PIL.Image.Image: The merged image grid.
    """
    # Calculate number of columns based on number of rows and images
    ncol = (len(images) + nrow - 1) // nrow

    # Get size of each image in pixels
    image_width, image_height = images[0].size

    # Create new image to hold the grid
    grid_width = ncol * image_width + (ncol - 1) * gap
    grid_height = nrow * image_height + (nrow - 1) * gap
    grid_image = Image.new("RGB", (grid_width, grid_height), color="white")

    # Paste images into grid
    for i, image in enumerate(images):
        row = i // ncol
        col = i % ncol
        x = col * (image_width + gap)
        y = row * (image_height + gap)
        grid_image.paste(image, (x, y))

    return grid_image
