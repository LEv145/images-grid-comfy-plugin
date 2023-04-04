import typing as t


class BasePlotNode():
    CATEGORY: str = "XYPlot"
    FUNCTION: str = "execute"


Image = t.Any
FloatImage = list[Image]
