# from buffer_api.inputs.platforms.facebook.consts import PLATFORM
# from buffer_api.inputs.platforms.base import _PlatformMetadataInput
# from buffer_api.enums import PostType
# from dataclasses import dataclass



# @dataclass(slots = True)
# class FacebookPostMedatadaInput(
#     _PlatformMetadataInput
# ):
#     """
#     Metadata for a facebook post that is a post.
#     """

#     platform = PLATFORM

#     type: PostType = PostType.REEL
#     first_comment: str = ''
#     """
#     The first comment we want to add to make the
#     people interact with the post, if we want it.
#     """

#     __graphql_field_map__ = {
#         'first_comment': 'firstComment',
#     }


# @dataclass(slots = True)
# class FacebookStoryMedatadaInput(
#     _PlatformMetadataInput
# ):
#     """
#     Metadata for a facebook post that is a story.
#     """

#     platform = PLATFORM

#     type: PostType = PostType.STORY