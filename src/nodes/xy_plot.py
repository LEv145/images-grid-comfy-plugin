import typing as t

from ..base import BasePlotNode, FloatImage, Image
from ..utils import tensor_to_pillow, pillow_to_tensor, create_image_grid


class XYPlotNode(BasePlotNode):
    RETURN_TYPES: t.Tuple[str] = ("IMAGE",)

    @classmethod
    def INPUT_TYPES(cls) -> t.Dict[str, t.Any]:
        return {
            "required": {
                "float_image": ("FLOAT_IMAGE",),
                "gap": ("INT", {"default": 0, "min": 0}),
                "nrow": ("INT", {"default": 1, "min": 1}),
            },
        }

    def execute(
        self,
        float_image: FloatImage,
        nrow: int,
        gap: int
    ) -> tuple[Image]:
        pillow_images = [tensor_to_pillow(i) for i in float_image]
        pillow_grid = create_image_grid(pillow_images, nrow=nrow, gap=gap)
        tensor_grid = pillow_to_tensor(pillow_grid)

        return (tensor_grid,)
