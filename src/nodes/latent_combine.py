import typing as t

import torch

from ..base import BaseNode, Image


class LatentCombineNode(BaseNode):
    RETURN_TYPES: tuple[str] = ("LATENT",)

    @classmethod
    def INPUT_TYPES(cls) -> dict[str, t.Any]:
        return {
            "required": {
                "latent_1": ("LATENT",),
                "latent_2": ("LATENT",),
            },
        }

    def execute(
        self,
        latent_1: dict[str, t.Any],
        latent_2: dict[str, t.Any],
    ) -> tuple[dict[str, t.Any]]:
        samples = torch.cat((latent_1["samples"], latent_2["samples"]), 0)

        return ({"samples": samples},)
