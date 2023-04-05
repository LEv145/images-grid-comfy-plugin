import typing as t

from ..base import BasePlotNode, Image


class ImageSetAreaNode(BasePlotNode):
    RETURN_TYPES: t.Tuple[str] = ("IMAGES",)

    @classmethod
    def INPUT_TYPES(cls) -> t.Dict[str, t.Any]:
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    def execute(self, image: Image) -> t.Tuple[t.List[Image]]:
        return ([image],)
