"""
These sticker fields are just for the
reminder option, which is a notification
sent to your phone to go to the app, copy
the content and publish it faster, but
cannot be used with scheduled posts.

Each post type will have its own sticker
fields input class, including only the
fields that are accepted by that type.

Check this:
- https://developers.buffer.com/types/InstagramStickerFields.html
"""
from bufferpy.graphql.types import _GraphQLInput
from dataclasses import dataclass


@dataclass(slots = True)
class InstagramReelStickerFieldsInput(
    _GraphQLInput
):
    """
    The sticker fields for the instagram post
    of the 'reel' type. It can be used only for
    reminders.

    These stickers include these fields:
    - `music`
    - `display_text`
    - `topics`
    - `products`
    """
    
    __graphql_field_map__ = {
        'display_text': 'text'
    }

    music: str = ''
    """
    The music text we want to display.
    """
    display_text: str = ''
    """
    The text that will be displayed over the 
    multimedia content during the whole video.
    """
    topics: str = ''
    """
    The topics the post is about.

    TODO: How, as a list and we separate it by
    commas (?)
    """
    products: str = ''
    """
    The product links that will be linked in
    the post.

    TODO: How, as a list of links (?)
    """


@dataclass(slots = True)
class InstagramPostStickerFieldsInput(
    _GraphQLInput
):
    """
    The sticker fields for the instagram post
    of the 'post' type. It can be used only for
    reminders.

    These stickers include these fields:
    - `music`
    - `products`
    """

    music: str = ''
    """
    The music text we want to display.
    """
    products: str = ''
    """
    The product links that will be linked in
    the post.

    TODO: How, as a list of links (?)
    """


@dataclass(slots = True)
class InstagramStoryStickerFieldsInput(
    _GraphQLInput
):
    """
    The sticker fields for the instagram post
    of the 'story' type. It can be used only for
    reminders.

    These stickers include these fields:
    - `music`
    - `display_text`
    - `other`
    """

    __graphql_field_map__ = {
        'display_text': 'text'
    }

    music: str = ''
    """
    The music text we want to display.
    """
    display_text: str = ''
    """
    The text that will be displayed over the 
    multimedia content during the whole video.
    """
    other: str = ''
    """
    TODO: They say this, but I don't know:
    'Additional field for any other post content'
    """