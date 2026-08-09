from bufferpy.inputs import CreatePostInput
from bufferpy.inputs.assets import VideoAssetInput
from bufferpy.enums import ShareMode, SchedulingType
from bufferpy.inputs.dataclasses import PublicationDate
from bufferpy.inputs.platforms.tiktok.posts import TiktokReelMetadataInput
from bufferpy.inputs.platforms.tiktok.reminders import TiktokReelReminderMetadataInput
from typing import Union


class _Tiktok:
    """
    *For internal use only*

    Internal class to simplify wrapping the
    functionality related to the Tiktok channel.
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
        publish_at: Union[PublicationDate, None],
        # specific fields
        is_ai_generated: bool = False,
    ):
        """
        Schedule a Tiktok reel to be published
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
        metadata = TiktokReelMetadataInput(
            is_ai_generated = is_ai_generated,
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


    def schedule_reel_notification(
        self,
        # TODO: Refactor so the instance knows the channel (?)
        channel_id: str,
        video_url: str,
        text: str,
        publish_at: Union[PublicationDate, None]
    ):
        """
        Schedule a Tiktok reel notification to be
        sent to your phone at the `publish_at` date
        provided, or inmediately if `None`.
        """
        # Scheduled reminder notification must be like this
        scheduling_type = SchedulingType.NOTIFICATION
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
        metadata = TiktokReelReminderMetadataInput()

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