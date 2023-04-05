import typing as t

from ..base import BasePlotNode, Image


class FloatImageCombineNode(BasePlotNode):
    RETURN_TYPES: t.Tuple[str] = ("IMAGES",)

    @classmethod
    def INPUT_TYPES(cls) -> t.Dict[str, t.Any]:
        return {
            "required": {
                "float_image_1": ("IMAGES",),
                "float_image_2": ("IMAGES",),
            },
        }

    def execute(
        self,
        float_image_1: t.List[Image],
        float_image_2: t.List[Image],
    ) -> t.Tuple[t.List[Image]]:
        return (float_image_1 + float_image_2,)
