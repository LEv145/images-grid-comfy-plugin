import typing as t

import torch

from ..base import BaseNode


class LatentCombineNode(BaseNode):
    RETURN_TYPES: tuple[str, ...] = ("LATENT",)

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
        latent_1: dict[str, torch.Tensor],
        latent_2: dict[str, torch.Tensor],
    ) -> tuple[dict[str, torch.Tensor]]:
        samples = torch.cat((latent_1["samples"], latent_2["samples"]), 0)

        return ({"samples": samples},)
