import typing as t

from ..base import BaseNode, Image
from ..utils import (
    tensor_to_pillow,
    pillow_to_tensor,
    create_image_grid_by_columns,
    create_image_grid_by_rows,
)


class BaseImagesGridNode(BaseNode):
    RETURN_TYPES: t.Tuple[str] = ("IMAGE",)

    @classmethod
    def _create_input_types(cls, coordinate_name: str) -> t.Dict[str, t.Any]:
        return {
            "required": {
                "images": ("IMAGE",),
                "gap": ("INT", {"default": 0, "min": 0}),
                coordinate_name: ("INT", {"default": 1, "min": 1}),
            }
        }

    def _create_execute(self, images, function, function_kw) -> t.Tuple[Image]:
        pillow_images = [tensor_to_pillow(i) for i in images]
        pillow_grid = function(images=pillow_images, **function_kw)
        tensor_grid = pillow_to_tensor(pillow_grid)

        return (tensor_grid,)


class ImagesGridByColumnsNode(BaseImagesGridNode):
    @classmethod
    def INPUT_TYPES(cls) -> t.Dict[str, t.Any]:
        return cls._create_input_types("max_columns")

    def execute(self, images: Image, **kw) -> tuple[Image]:
        return self._create_execute(images, create_image_grid_by_columns, kw)


class ImagesGridByRowsNode(BaseImagesGridNode):
    @classmethod
    def INPUT_TYPES(cls) -> t.Dict[str, t.Any]:
        return cls._create_input_types("max_rows")

    def execute(self, images: Image, **kw) -> tuple[Image]:
        return self._create_execute(images, create_image_grid_by_rows, kw)
