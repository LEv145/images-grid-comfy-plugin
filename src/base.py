import typing as t
from pathlib import Path


STATIC_PATH = Path(__file__).parent.parent / "static"


class BaseNode():
    CATEGORY: str = "ImagesGrid"
    FUNCTION: str = "execute"
