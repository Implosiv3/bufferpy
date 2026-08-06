from bufferpy.graphql.types import _GraphQLInput
from dataclasses import dataclass
from typing import Any


@dataclass(slots = True)
class VideoAssetInput(
    _GraphQLInput
):
    """
    The `url` to the video asset.
    """

    url: str

    def to_graphql(
        self
    ) -> dict[str, Any]:
        return {
            'video': {
                'url': self.url,
            }
        }


@dataclass(slots = True)
class ImageAssetInput(
    _GraphQLInput
):
    """
    The `url` to the image asset.
    """

    url: str

    def to_graphql(
        self
    ) -> dict[str, Any]:
        return {
            'image': {
                'url': self.url,
            }
        }