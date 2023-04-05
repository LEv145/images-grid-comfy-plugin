import typing as t

import torch

from ..base import BaseNode, Image


class ImageCombineNode(BaseNode):
    RETURN_TYPES: t.Tuple[str] = ("IMAGE",)

    @classmethod
    def INPUT_TYPES(cls) -> t.Dict[str, t.Any]:
        return {
            "required": {
                "image_1": ("IMAGE",),
                "image_2": ("IMAGE",),
            },
        }

    def execute(
        self,
        image_1: Image,
        image_2: Image,
    ) -> t.Tuple[Image]:
        print(image_1.size())
        print(image_2.size())
        print(image_1)

        result = torch.cat((image_1, image_2), 0)
        print(result.size())

        return (result,)
