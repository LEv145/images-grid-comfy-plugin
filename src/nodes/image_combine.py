import typing as t

import torch

from ..base import BaseNode


class ImageCombineNode(BaseNode):
    RETURN_TYPES: tuple[str, ...] = ("IMAGE",)

    @classmethod
    def INPUT_TYPES(cls) -> dict[str, t.Any]:
        return {
            "required": {
                "image_1": ("IMAGE",),
                "image_2": ("IMAGE",),
            },
        }

    def execute(
        self,
        image_1: torch.Tensor,
        image_2: torch.Tensor,
    ) -> tuple[torch.Tensor]:
        result = torch.cat((image_1, image_2), 0)

        return (result,)
