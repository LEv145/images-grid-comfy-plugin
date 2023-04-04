import typing as t

from ..base import BasePlotNode, FloatImage


class FloatImageCombineNode(BasePlotNode):
    RETURN_TYPES: t.Tuple[str] = ("FLOAT_IMAGE",)

    @classmethod
    def INPUT_TYPES(cls) -> t.Dict[str, t.Any]:
        return {
            "required": {
                "float_image_1": ("FLOAT_IMAGE",),
                "float_image_2": ("FLOAT_IMAGE",),
            },
        }

    def execute(self, float_image_1: FloatImage, float_image_2: FloatImage) -> tuple[FloatImage]:
        return (float_image_1 + float_image_2,)
