import typing as t

from nodes import KSamplerAdvanced  # type: ignore

from ..base import BasePlotNode, Image, KSamplerXYPlotInput


class KSamplerXYPlotNode(BasePlotNode):
    RETURN_TYPES: t.Tuple[str] = ("IMAGES",)

    def __init__(self) -> None:
        self._sampler = KSamplerAdvanced()

    @classmethod
    def INPUT_TYPES(cls):
        result = KSamplerAdvanced.INPUT_TYPES()
        result["required"]["vae"] = ("VAE", )
        #result["required"]["x_items"] = ("XYPlotItem",)
        #result["required"]["y_items"] = ("XYPlotItem",)
        return result

    def execute(
        self,
        vae,
        #x_items,
        #y_items,
        **sampler_kw,
    ) -> tuple[t.List[Image]]:
        x_items = [
            KSamplerXYPlotInput(value=1, setting="cfg"),
            KSamplerXYPlotInput(value=2, setting="cfg"),
        ]
        y_items = [
            KSamplerXYPlotInput(value=1, setting="noise_seed"),
            KSamplerXYPlotInput(value=2, setting="noise_seed"),
        ]

        latents = self._sample_latents(
            x_items=x_items,
            y_items=y_items,
            sampler_kw=sampler_kw,
        )
        result = list(self._decode_latents(latents=latents, vae=vae))
        print(result)
        print(type(result[0]))

        return (result,)

    def _sample_latents(self, x_items, y_items, sampler_kw):
        for x in x_items:
            for y in y_items:
                sampler_settings = sampler_kw.copy()
                sampler_settings[x.setting] = x.value
                sampler_settings[y.setting] = y.value

                yield self._sampler.sample(**sampler_settings)[0]

    def _decode_latents(self, latents, vae) -> t.Iterable[Image]:
        return (
            vae.decode(i["samples"])
            for i in latents
        )
