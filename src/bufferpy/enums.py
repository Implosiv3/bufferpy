"""
Information extracted from the official API and
their AI chat agent.
"""
from bufferpy.graphql.builder import GraphQLEnum


class ShareMode(
    GraphQLEnum
):
    """
    The date and time in which you want your post to
    be shared.

    Obtained from here:
    - https://developers.buffer.com/types/ShareMode.html
    """
    ADD_TO_QUEUE = 'addToQueue'
    """
    This adds the post to your existing posting
    schedule. It will be placed in the next available
    time slot according to the posting plan you have
    set up for that specific channel.
    I am not sure).
    """
    CUSTOM_SCHEDULED = 'customScheduled'
    """
    Use this when you want to set a specific, manual
    date and time for your post to be published
    rather than relying on your pre-set queue slots.

    You will need to provide a `dueAt` date in the
    ISO 8601 format (UTC).
    """
    SHARE_NEXT = 'shareNext'
    """
    This option places the post at the very top of
    your queue, essentially "bumping" it to be the
    next piece of content published when the next
    available slot opens.
    """
    SHARE_NOW = 'shareNow'
    """
    As the name suggests, this instructs Buffer to
    publish the post immediately, bypassing any
    queue or scheduled time.
    """


class SchedulingType(
    GraphQLEnum
):
    """
    Controls how that post is ultimately
    delivered.

    Obtained from here:
    - https://developers.buffer.com/types/SchedulingType.html
    """
    AUTOMATIC = 'automatic'
    """
    This is the standard mode where Buffer's
    publishing workers send the post to your
    social channel automatically at the
    scheduled time, with no action required
    from you.

    When we want the post to be published
    automatically.
    """
    NOTIFICATION = 'notification'
    """
    In this mode, Buffer does not publish
    the post directly. Instead, it sends a
    reminder (a notification) to you at the
    scheduled time, prompting you to publish
    the post manually.
    """


class PostType(
    GraphQLEnum
):
    """
    The type of post you want to publish.

    A setting that specifies the format or
    content structure of a post. Because
    different social networks support unique
    features—such as Instagram's Reels and
    Stories versus LinkedIn's carousel
    posts—PostType is used to ensure the
    post is processed and formatted
    correctly for the specific destination
    channel.
    
    Obtained from here:
    - https://developers.buffer.com/types/PostType.html
    """
    # TODO: Specify which platform accepts each
    POST = 'post'
    STORY = 'story'
    REEL = 'reel'
    # TODO: These below are not supported by now
    # CAROUSEL = 'carousel'
    # EVENT = 'event'
    # GHOST_POST = 'ghost_post'
    # OFFER = 'offer'
    # SHORT = 'short'
    # THREAD = 'thread'
    # WHATS_NEW = 'whats_new'