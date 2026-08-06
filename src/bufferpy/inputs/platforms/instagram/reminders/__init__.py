"""
Instagram reminders, which are notifications that
will be sent to your phone so you can manually
publish the post by yourself.

These reminders include the stickers optional
metadata values that you can find in the
`stickers.py` module.
"""
from bufferpy.inputs.platforms.instagram.reminders.stickers import InstagramPostStickerFieldsInput, InstagramReelStickerFieldsInput, InstagramStoryStickerFieldsInput
from bufferpy.inputs.platforms.instagram.consts import PLATFORM
from bufferpy.enums import PostType
from bufferpy.inputs.platforms.base import _PlatformMetadataInput
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass(slots = True)
class InstagramReelReminderMetadataInput(
    _PlatformMetadataInput
):
    """
    Metadata for an instagram post reminder that 
    will be a reel.
    """

    platform: ClassVar[str] = PLATFORM
    type: PostType = field(default = PostType.REEL, init = False)

    do_share_to_feed: bool = True
    """
    Boolean flag to indicate if the post has to
    be shared to the feed or not.

    _It doesn't appear in the web app..._
    """
    # TODO: Paid plan required
    # first_comment: str = ''
    # """
    # The first comment we want to add to make the
    # people interact with the post, if we want it.
    # """
    sticker_fields: InstagramReelStickerFieldsInput = field(
        default_factory = InstagramReelStickerFieldsInput
    )

    __graphql_field_map__ = {
        'do_share_to_feed': 'shouldShareToFeed',
        # TODO: Paid plan required
        # 'first_comment': 'firstComment',
        'sticker_fields': 'stickerFields'
    }

    # Due to bug in python 3.10...
    def __post_init__(
        self
    ):
        object.__setattr__(self, 'type', PostType.REEL)


@dataclass(slots = True)
class InstagramPostReminderMetadataInput(
    _PlatformMetadataInput
):
    """
    Metadata for an instagram post reminder that 
    will be a post.
    """

    platform: ClassVar[str] = PLATFORM
    type: PostType = field(default = PostType.POST, init = False)

    do_share_to_feed: bool = True
    """
    Boolean flag to indicate if the post has to
    be shared to the feed or not.

    _It doesn't appear in the web app..._
    """
    # TODO: Paid plan required
    # first_comment: str = ''
    # """
    # The first comment we want to add to make the
    # people interact with the post, if we want it.
    # """
    sticker_fields: InstagramPostStickerFieldsInput = field(
        default_factory = InstagramPostStickerFieldsInput
    )

    __graphql_field_map__ = {
        'do_share_to_feed': 'shouldShareToFeed',
        'first_comment': 'firstComment',
        'sticker_fields': 'stickerFields'
    }

    # Due to bug in python 3.10...
    def __post_init__(
        self
    ):
        object.__setattr__(self, 'type', PostType.POST)


@dataclass(slots = True)
class InstagramStoryReminderMetadataInput(
    _PlatformMetadataInput
):
    """
    Metadata for an instagram post reminder that 
    will be a story.
    """

    platform: ClassVar[str] = PLATFORM
    type: PostType = field(default = PostType.STORY, init = False)

    do_share_to_feed: bool = True
    """
    Boolean flag to indicate if the post has to
    be shared to the feed or not.

    _It doesn't appear in the web app..._
    """
    link: str = ''
    """
    A link that we want to display in the story.

    _This value is weird, looks like a sticker
    but its not a sticker in the data..._
    """
    sticker_fields: InstagramStoryStickerFieldsInput = field(
        default_factory = InstagramStoryStickerFieldsInput
    )

    __graphql_field_map__ = {
        'do_share_to_feed': 'shouldShareToFeed',
        'sticker_fields': 'stickerFields'
    }

    # Due to bug in python 3.10...
    def __post_init__(
        self
    ):
        object.__setattr__(self, 'type', PostType.STORY)