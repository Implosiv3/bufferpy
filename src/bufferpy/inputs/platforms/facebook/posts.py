"""
The functionality related to Facebook.

The Buffer platform API only allows you to
schedule posts that will be automatically
published, but not to create reminders.

Check the official docummentation here:
- https://developers.buffer.com/types/FacebookPostMetadata.html
"""
from bufferpy.inputs.platforms.facebook.consts import PLATFORM
from bufferpy.inputs.platforms.base import _PlatformMetadataInput
from bufferpy.enums import PostType
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass(slots = True)
class FacebookReelMedatadaInput(
    _PlatformMetadataInput
):
    """
    Metadata for a Facebook post that is a reel.
    """

    platform: ClassVar[str] = PLATFORM
    type: PostType = field(default = PostType.REEL, init = False)

    # Due to bug in python 3.10...
    def __post_init__(
        self
    ):
        object.__setattr__(self, 'type', PostType.REEL)


@dataclass(slots = True)
class FacebookPostMedatadaInput(
    _PlatformMetadataInput
):
    """
    Metadata for a Facebook post that is a post.
    """

    platform: ClassVar[str] = PLATFORM
    type: PostType = field(default = PostType.POST, init = False)

    # TODO: Paid plan required
    # first_comment: str = ''
    # """
    # The first comment we want to add to make the
    # people interact with the post, if we want it.
    # """

    # __graphql_field_map__ = {
    #     # TODO: Paid plan required
    #     # 'first_comment': 'firstComment',
    # }

    # Due to bug in python 3.10...
    def __post_init__(
        self
    ):
        object.__setattr__(self, 'type', PostType.POST)


@dataclass(slots = True)
class FacebookStoryMedatadaInput(
    _PlatformMetadataInput
):
    """
    Metadata for a Facebook post that is a story.
    """

    platform: ClassVar[str] = PLATFORM
    type: PostType = field(default = PostType.STORY, init = False)

    # Due to bug in python 3.10...
    def __post_init__(
        self
    ):
        object.__setattr__(self, 'type', PostType.STORY)