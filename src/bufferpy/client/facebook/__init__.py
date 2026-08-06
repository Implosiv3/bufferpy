



from bufferpy.client.utils import build_datetime
from bufferpy.enums import SchedulingType, ShareMode
from bufferpy.inputs import CreatePostInput
from bufferpy.inputs.assets import ImageAssetInput, VideoAssetInput
from bufferpy.inputs.platforms.facebook.posts import FacebookReelMedatadaInput, FacebookPostMedatadaInput, FacebookStoryMedatadaInput


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
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        # specific fields
        # TODO: Paid plan required
        # first_comment: str = '',
    ):
        """
        Schedule an instagram reel to be published
        automatically.
        """
        # Scheduled post must be like this
        scheduling_type = SchedulingType.AUTOMATIC
        mode = ShareMode.CUSTOM_SCHEDULED
        publish_at = build_datetime(year, month, day, hour, minute)

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
            due_at = publish_at,
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
        # date below
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        # specific fields
        # TODO: Paid plan required
        # first_comment: str = '',
    ):
        """
        Schedule an instagram post to be published
        automatically.
        """
        # Scheduled post must be like this
        scheduling_type = SchedulingType.AUTOMATIC
        mode = ShareMode.CUSTOM_SCHEDULED
        publish_at = build_datetime(year, month, day, hour, minute)

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
            due_at = publish_at,
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
        # date below
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        # specific fields
        # TODO: This doesn't appear in the web app
        # do_share_to_feed: bool = True,
        # is_ai_generated: bool = False,
        # TODO: Paid plan required
        # first_comment: str = '',
    ):
        """
        Schedule a Facebook story to be published
        automatically.
        """
        # Scheduled post must be like this
        scheduling_type = SchedulingType.AUTOMATIC
        mode = ShareMode.CUSTOM_SCHEDULED
        publish_at = build_datetime(year, month, day, hour, minute)

        # Metadata
        metadata = FacebookStoryMedatadaInput(
            # TODO: This doesn't appear in the web app
            # do_share_to_feed = do_share_to_feed,
            # is_ai_generated = is_ai_generated,
            # TODO: Paid plan required
            # first_comment = first_comment,
        )

        input_data = CreatePostInput(
            channel_id = channel_id,
            text = text,
            mode = mode,
            metadata = metadata,
            scheduling_type = scheduling_type,
            due_at = publish_at,
            # TODO: It should be more than 1 asset
            assets = [
                ImageAssetInput(
                    url = image_url,
                )
            ],
        )

        return self._buffer_client._schedule_post(input_data)