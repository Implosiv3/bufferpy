from bufferpy.enums import SchedulingType, ShareMode, PostType
from bufferpy.graphql.types import _GraphQLInput
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Union


"""
TODO: Create a specific MetadataInput for each
type of post and channel, because there are
different fields depending on it. The 'title'
is only valid, on Facebook, when it is a post 
and not a story nor a reel. We need to make it
more strict or it will be a mess. It has to be
easy to use.

TODO: Move to 'inputs.instagram', 'inputs.tiktok',
etc.
"""
@dataclass(slots = True)
class InstagramPostMetadataInput(
    _GraphQLInput
):
    """
    Check it here:
    - https://developers.buffer.com/types/InstagramPostMetadata.html
    """

    __graphql_field_map__ = {
        'should_share_to_feed': 'shouldShareToFeed',
    }

    type: PostType
    # TODO: 'should...' is only for 'REEL', no 'POST', no 'STORY'
    should_share_to_feed: bool = True
    """
    To share it or not in the feed.
    """

    def to_graphql(
        self
    ) -> dict[str, Any]:
        return {
            'instagram': _GraphQLInput.to_graphql(self)
        }


@dataclass(slots = True)
class FacebookPostMedatadaInput(
    _GraphQLInput
):
    """
    Check it here:
    - https://developers.buffer.com/types/FacebookPostMetadata.html
    """

    type: PostType
    # TODO: 'title' is only for 'POST' no 'REEL' no 'STORY'
    # title: str = ''
    """
    The title of the reel
    """

    def to_graphql(
        self
    ) -> dict[str, Any]:
        return {
            'facebook': _GraphQLInput.to_graphql(self)
        }


@dataclass(slots = True)
class TiktokPostMedatadaInput(
    _GraphQLInput
):
    """
    Check it here:
    - https://developers.buffer.com/types/TiktokPostMetadata.html
    """

    # TODO: There is only one type available 'POST'
    # type: PostType
    # TODO: 'title' is only for 'POST' that includes image, no video
    # title: str = ''
    """
    The title of the post
    """
    is_ai_generated: bool = False

    __graphql_field_map__ = {
        'is_ai_generated': 'isAiGenerated'
    }

    def to_graphql(
        self
    ) -> dict[str, Any]:
        # Force post, is the only option
        self.type = PostType.POST

        return {
            'tiktok': _GraphQLInput.to_graphql(self)
        }


@dataclass(slots = True)
class CreatePostInput(
    _GraphQLInput
):
    __graphql_field_map__ = {
        'channel_id': 'channelId',
        'due_at': 'dueAt',
        'scheduling_type': 'schedulingType',
    }

    channel_id: str
    text: str = ''
    assets: list[_GraphQLInput] = field(default_factory = list)
    mode: ShareMode = ShareMode.CUSTOM_SCHEDULED
    metadata: Union[InstagramPostMetadataInput, FacebookPostMedatadaInput, None] = None
    scheduling_type: SchedulingType = SchedulingType.AUTOMATIC
    due_at: Union[datetime, None] = None

