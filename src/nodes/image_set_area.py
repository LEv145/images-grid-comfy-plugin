import typing as t

from ..base import BasePlotNode, FloatImage, Image


class ImageSetAreaNode(BasePlotNode):
    RETURN_TYPES: t.Tuple[str] = ("FLOAT_IMAGE",)

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> t.Dict[str, t.Any]:
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    def execute(self, image: Image) -> tuple[FloatImage]:
        return ([image],)
