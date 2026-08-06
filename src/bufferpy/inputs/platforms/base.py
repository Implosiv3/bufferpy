from bufferpy.graphql.types import _GraphQLInput
from typing import Any, ClassVar


class _PlatformMetadataInput(
    _GraphQLInput
):
    """
    *For internal use only*

    The base class for the metadata we will
    include in a post.
    """

    platform: ClassVar[str]

    def to_graphql(
        self
    ) -> dict[str, Any]:
        return {
            self.platform: _GraphQLInput.to_graphql(self)
        }
        