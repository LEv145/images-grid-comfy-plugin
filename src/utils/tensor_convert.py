import typing as t

import torch
import numpy as np
from PIL import Image


def tensor_to_pillow(image: t.Any) -> Image.Image:
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def pillow_to_tensor(image: Image.Image) -> t.Any:
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)
