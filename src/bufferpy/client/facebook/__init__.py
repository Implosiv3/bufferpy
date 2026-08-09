from bufferpy.inputs.platforms.facebook.posts import FacebookReelMedatadaInput, FacebookPostMedatadaInput, FacebookStoryMedatadaInput
from bufferpy.inputs import CreatePostInput
from bufferpy.inputs.assets import ImageAssetInput, VideoAssetInput
from bufferpy.inputs.dataclasses import PublicationDate
from bufferpy.enums import SchedulingType, ShareMode
from typing import Union


class _Facebook:
    """
    *For internal use only*

    Internal class to simplify wrapping the
    functionality related to the Facebook channel.
    """

    def __init__(
        self,
        buffer_client: 'BufferClient'
    ):
        self._buffer_client: 'BufferClient' = buffer_client
        """
        *For internal use only*

        The parent `BufferClient` reference to do the
        tasks we need to do.
        """


    def schedule_reel_post(
        self,
        # TODO: Refactor so the instance knows the channel (?)
        channel_id: str,
        video_url: str,
        text: str,
        # date below
        publish_at: Union[PublicationDate, None],
        # specific fields
        # TODO: Paid plan required
        # first_comment: str = '',
    ):
        """
        Schedule an instagram reel to be published
        automatically at the `publish_at` date
        provided, or inmediately if `None`.
        """
        # Scheduled post must be like this
        scheduling_type = SchedulingType.AUTOMATIC
        mode = (
            ShareMode.CUSTOM_SCHEDULED
            if publish_at is not None else
            ShareMode.SHARE_NOW
        )
        due_at = (
            publish_at.as_iso8601
            if publish_at is not None else
            None
        )

        # Metadata
        metadata = FacebookReelMedatadaInput(
            # TODO: Paid plan required
            # first_comment = first_comment,
        )

        input_data = CreatePostInput(
            channel_id = channel_id,
            text = text,
            mode = mode,
            metadata = metadata,
            scheduling_type = scheduling_type,
            due_at = due_at,
            assets = [
                VideoAssetInput(
                    url = video_url,
                )
            ],
        )

        return self._buffer_client._schedule_post(input_data)

    
    def schedule_post_post(
        self,
        # TODO: Refactor so the instance knows the channel (?)
        channel_id: str,
        # TODO: It could be more than 1 url
        image_url: str,
        text: str,
        publish_at: Union[PublicationDate, None],
        # specific fields
        # TODO: Paid plan required
        # first_comment: str = '',
    ):
        """
        Schedule an instagram post to be published
        automatically at the `publish_at` date
        provided, or inmediately if `None`.
        """
        # Scheduled post must be like this
        scheduling_type = SchedulingType.AUTOMATIC
        mode = (
            ShareMode.CUSTOM_SCHEDULED
            if publish_at is not None else
            ShareMode.SHARE_NOW
        )
        due_at = (
            publish_at.as_iso8601
            if publish_at is not None else
            None
        )

        # Metadata
        metadata = FacebookPostMedatadaInput(
            # TODO: Paid plan required
            # first_comment = first_comment,
        )

        input_data = CreatePostInput(
            channel_id = channel_id,
            text = text,
            mode = mode,
            metadata = metadata,
            scheduling_type = scheduling_type,
            due_at = due_at,
            # TODO: It should be more than 1 asset
            assets = [
                ImageAssetInput(
                    url = image_url,
                )
            ],
        )

        return self._buffer_client._schedule_post(input_data)


    def schedule_story_post(
        self,
        # TODO: Refactor so the instance knows the channel (?)
        channel_id: str,
        # TODO: It could be more than 1 url
        image_url: str,
        text: str,
        publish_at: Union[PublicationDate, None],
        # specific fields
        # TODO: Paid plan required
        # first_comment: str = '',
    ):
        """
        Schedule a Facebook story to be published
        automatically at the `publish_at` date
        provided, or inmediately if `None`.
        """
        # Scheduled post must be like this
        scheduling_type = SchedulingType.AUTOMATIC
        mode = (
            ShareMode.CUSTOM_SCHEDULED
            if publish_at is not None else
            ShareMode.SHARE_NOW
        )
        due_at = (
            publish_at.as_iso8601
            if publish_at is not None else
            None
        )

        # Metadata
        metadata = FacebookStoryMedatadaInput(
            # TODO: Paid plan required
            # first_comment = first_comment,
        )

        input_data = CreatePostInput(
            channel_id = channel_id,
            text = text,
            mode = mode,
            metadata = metadata,
            scheduling_type = scheduling_type,
            due_at = due_at,
            # TODO: It should be more than 1 asset
            assets = [
                ImageAssetInput(
                    url = image_url,
                )
            ],
        )

        return self._buffer_client._schedule_post(input_data)