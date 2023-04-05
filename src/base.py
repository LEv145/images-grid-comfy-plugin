import typing as t
from dataclasses import dataclass


class BasePlotNode():
    CATEGORY: str = "XYPlot"
    FUNCTION: str = "execute"


@dataclass
class KSamplerXYPlotInput():
    setting: str
    value: int


Image = t.Any
