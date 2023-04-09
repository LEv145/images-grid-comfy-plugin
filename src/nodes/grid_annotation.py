import typing as t

from PIL import ImageFont

from ..base import BaseNode, STATIC_PATH
from ..utils import Annotation


class GridAnnotationNode(BaseNode):
    RETURN_TYPES: tuple[str] = ("GRID_ANNOTATION",)

    @classmethod
    def INPUT_TYPES(cls) -> dict[str, t.Any]:
        return {
            "required": {
                "column_texts": ("STRING", {"multiline": False}),
                "row_texts": ("STRING", {"multiline": False}),
                "font_size": ("INT", {"default": 30, "min": 1}),
            },
        }

    def execute(
        self,
        column_texts: str,
        row_texts: str,
        font_size: int,
    ) -> tuple[Annotation]:
        font = ImageFont.truetype(str(STATIC_PATH / "Roboto-Regular.ttf"), size=font_size)
        column_texts_list = self._set_value_to_texts_list(
            self._get_texts_from_string(column_texts),
        )
        row_texts_list = self._set_value_to_texts_list(
            self._get_texts_from_string(row_texts),
        )

        result = Annotation(column_texts=column_texts_list, row_texts=row_texts_list, font=font)
        return (result,)

    def _get_texts_from_string(self, string: str) -> list[str]:
        return [
            result
            for i in string.split(";")
            if (result := i.strip()) != ""
        ]

    def _set_value_to_texts_list(self, texts_list: list[str]) -> list[str]:
        if not texts_list:
            return ["None"]
        return texts_list
