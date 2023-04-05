import typing as t

import torch

from ..base import BaseNode, Image


class LatentCombineNode(BaseNode):
    RETURN_TYPES: t.Tuple[str] = ("LATENT",)

    @classmethod
    def INPUT_TYPES(cls) -> t.Dict[str, t.Any]:
        return {
            "required": {
                "latent_1": ("LATENT",),
                "latent_2": ("LATENT",),
            },
        }

    def execute(
        self,
        latent_1: t.Dict[str, t.Any],
        latent_2: t.Dict[str, t.Any],
    ) -> t.Tuple[t.Dict[str, t.Any]]:
        samples = torch.cat((latent_1["samples"], latent_2["samples"]), 0)

        return ({"samples": samples},)
