import typing as t

import torch

from ..base import BaseNode
from ..utils import (
    tensor_to_pillow,
    pillow_to_tensor,
    create_images_grid_by_columns,
    create_images_grid_by_rows,
    Annotation,
)

class BaseImagesGridNode(BaseNode):
    RETURN_TYPES: tuple[str] = ("IMAGE",)

    @classmethod
    def _create_input_types(cls, coordinate_name: str) -> dict[str, t.Any]:
        return {
            "required": {
                "images": ("IMAGE",),
                "gap": ("INT", {"default": 0, "min": 0}),
                coordinate_name: ("INT", {"default": 1, "min": 1}),
            },
            "optional": {
                "annotation": ("GRID_ANNOTATION",),
            }
        }

    def _create_execute(
        self,
        function: t.Callable,
        \
        images: torch.Tensor,
        gap: int,
        annotation: Annotation | None = None,
        **kw,
    ) -> tuple[torch.Tensor]:
        pillow_images = [tensor_to_pillow(i) for i in images]
        pillow_grid = function(
            images=pillow_images,
            gap=gap,
            annotation=annotation,
            **kw,
        )
        tensor_grid = pillow_to_tensor(pillow_grid)

        return (tensor_grid,)


class ImagesGridByColumnsNode(BaseImagesGridNode):
    @classmethod
    def INPUT_TYPES(cls) -> dict[str, t.Any]:
        return cls._create_input_types("max_columns")

    def execute(self, **kw) -> tuple[torch.Tensor]:
        return self._create_execute(create_images_grid_by_columns, **kw)


class ImagesGridByRowsNode(BaseImagesGridNode):
    @classmethod
    def INPUT_TYPES(cls) -> dict[str, t.Any]:
        return cls._create_input_types("max_rows")

    def execute(self, **kw) -> tuple[torch.Tensor]:
        return self._create_execute(create_images_grid_by_rows, **kw)
