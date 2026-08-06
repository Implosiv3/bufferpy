from bufferpy.client.utils import build_datetime
from bufferpy.inputs import CreatePostInput
from bufferpy.inputs.assets import VideoAssetInput
from bufferpy.enums import ShareMode, SchedulingType
from bufferpy.inputs.platforms.tiktok.posts import TiktokReelMetadataInput
from bufferpy.inputs.platforms.tiktok.reminders import TiktokReelReminderMetadataInput


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
        # date below
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        # specific fields
        is_ai_generated: bool = False,
    ):
        """
        Schedule a Tiktok reel to be published
        automatically.
        """
        # Scheduled post must be like this
        scheduling_type = SchedulingType.AUTOMATIC
        mode = ShareMode.CUSTOM_SCHEDULED
        publish_at = build_datetime(year, month, day, hour, minute)

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
            due_at = publish_at,
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
        # date below
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
    ):
        """
        Schedule a Tiktok reel notification to be
        sent to your phone at the time you say as a
        reminder.
        """
        # Scheduled reminder notification must be like this
        scheduling_type = SchedulingType.NOTIFICATION
        mode = ShareMode.CUSTOM_SCHEDULED
        publish_at = build_datetime(year, month, day, hour, minute)

        # Metadata
        metadata = TiktokReelReminderMetadataInput()

        input_data = CreatePostInput(
            channel_id = channel_id,
            text = text,
            mode = mode,
            metadata = metadata,
            scheduling_type = scheduling_type,
            due_at = publish_at,
            assets = [
                VideoAssetInput(
                    url = video_url,
                )
            ],
        )

        return self._buffer_client._schedule_post(input_data)