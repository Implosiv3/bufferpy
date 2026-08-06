from bufferpy.graphql.builder import GraphQLEnum


class ShareMode(
    GraphQLEnum
):
    """
    TODO: Explain it.

    Obtained from here:
    - https://developers.buffer.com/types/ShareMode.html
    """
    ADD_TO_QUEUE = 'addToQueue'
    """
    When we want the post to be published in the
    next available time spot (probably in 5 minutes,
    I am not sure).
    """
    CUSTOM_SCHEDULED = 'customScheduled'
    """
    When we will provide the `dueAt` date, the date
    in which it has to be published, in ISO 8601
    format (UTC).
    """
    SHARE_NEXT = 'shareNext'
    """
    TODO: Explain it.
    """
    SHARE_NOW = 'shareNow'
    """
    TODO: Explain it.
    """


class SchedulingType(
    GraphQLEnum
):
    """
    TODO: Explain it.

    Obtained from here:
    - https://developers.buffer.com/types/SchedulingType.html
    """
    AUTOMATIC = 'automatic'
    """
    When we want the post to be published
    automatically.
    """
    NOTIFICATION = 'notification'


class PostType(
    GraphQLEnum
):
    """
    The type of post you want to publish.
    
    Obtained from here:
    - https://developers.buffer.com/types/PostType.html
    """
    POST = 'post'
    STORY = 'story'
    REEL = 'reel'