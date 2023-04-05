import typing as t

from ..base import BasePlotNode, Image
from ..utils import tensor_to_pillow, pillow_to_tensor, create_image_grid


class XYPlotNode(BasePlotNode):
    RETURN_TYPES: t.Tuple[str] = ("IMAGE",)

    @classmethod
    def INPUT_TYPES(cls) -> t.Dict[str, t.Any]:
        return {
            "required": {
                "images": ("IMAGE",),
                "gap": ("INT", {"default": 0, "min": 0}),
                "ncol": ("INT", {"default": 1, "min": 1}),
            },
        }

    def execute(
        self,
        images: Image,
        ncol: int,
        gap: int
    ) -> tuple[Image]:
        pillow_images = [tensor_to_pillow(i) for i in images]
        pillow_grid = create_image_grid(pillow_images, ncol=ncol, gap=gap)
        tensor_grid = pillow_to_tensor(pillow_grid)

        return (tensor_grid,)
