from bufferpy.inputs.platforms.instagram.posts import InstagramReelMetadataInput, InstagramPostMetadataInput, InstagramStoryMetadataInput
from bufferpy.client.utils import build_datetime
from bufferpy.inputs.platforms.instagram.reminders import InstagramPostReminderMetadataInput, InstagramReelReminderMetadataInput, InstagramStoryReminderMetadataInput
from bufferpy.inputs.platforms.instagram.reminders.stickers import InstagramPostStickerFieldsInput, InstagramReelStickerFieldsInput, InstagramStoryStickerFieldsInput
from bufferpy.inputs import CreatePostInput
from bufferpy.inputs.assets import ImageAssetInput, VideoAssetInput
from bufferpy.enums import ShareMode, SchedulingType


class _Instagram:
    """
    *For internal use only*

    Internal class to simplify wrapping the
    functionality related to the Instagram channel.
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
        do_share_to_feed: bool = True,
        is_ai_generated: bool = False,
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
        metadata = InstagramReelMetadataInput(
            do_share_to_feed = do_share_to_feed,
            is_ai_generated = is_ai_generated,
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
        # specific fields
        # TODO: Paid plan required
        # first_comment: str = '',
        music: str = '',
        display_text: str = '',
        topics: str = '',
        products: str = '',
    ):
        """
        Schedule an instagram reel notification to be
        sent to your phone at the time you say as a
        reminder.
        """
        # Scheduled reminder notification must be like this
        scheduling_type = SchedulingType.NOTIFICATION
        mode = ShareMode.CUSTOM_SCHEDULED
        publish_at = build_datetime(year, month, day, hour, minute)

        # Metadata
        metadata = InstagramReelReminderMetadataInput(
            # This field is useless here but required...
            do_share_to_feed = True,
            # TODO: Paid plan required
            # first_comment = first_comment,
            sticker_fields = InstagramReelStickerFieldsInput(
                music = music,
                display_text = display_text,
                topics = topics,
                products = products
            )
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
        is_ai_generated: bool = False,
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
        metadata = InstagramPostMetadataInput(
            # This field is useless here but required...
            do_share_to_feed = True,    
            is_ai_generated = is_ai_generated,
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

    def schedule_post_notification(
        self,
        # TODO: Refactor so the instance knows the channel (?)
        channel_id: str,
        # TODO: It should be more than 1 asset
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
        music: str = '',
        # display_text: str = '',
        # topics: str = '',
        products: str = '',
    ):
        """
        Schedule an instagram post notification to be
        sent to your phone at the time you say as a
        reminder.
        """
        # Scheduled reminder notification must be like this
        scheduling_type = SchedulingType.NOTIFICATION
        mode = ShareMode.CUSTOM_SCHEDULED
        publish_at = build_datetime(year, month, day, hour, minute)

        # Metadata
        metadata = InstagramPostReminderMetadataInput(
            # This field is useless here but required...
            do_share_to_feed = True,    
            # TODO: Paid plan required
            # first_comment = first_comment,
            sticker_fields = InstagramPostStickerFieldsInput(
                music = music,
                # display_text = display_text,
                # topics = topics,
                products = products
            )
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
        is_ai_generated: bool = False,
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
        metadata = InstagramStoryMetadataInput(
            # This field is useless here but required...
            do_share_to_feed = True,
            is_ai_generated = is_ai_generated,
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


    def schedule_story_notification(
        self,
        # TODO: Refactor so the instance knows the channel (?)
        channel_id: str,
        # TODO: It should be more than 1 asset
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
        music: str = '',
        link: str = '',
        display_text: str = '',
        other: str = '',
    ):
        """
        Schedule an instagram post notification to be
        sent to your phone at the time you say as a
        reminder.
        """
        # Scheduled reminder notification must be like this
        scheduling_type = SchedulingType.NOTIFICATION
        mode = ShareMode.CUSTOM_SCHEDULED
        publish_at = build_datetime(year, month, day, hour, minute)

        # Metadata
        metadata = InstagramStoryReminderMetadataInput(
            # This field is useless here but required...
            do_share_to_feed = True,  
            link = link,
            # TODO: Paid plan required
            # first_comment = first_comment,
            sticker_fields = InstagramStoryStickerFieldsInput(
                music = music,
                # link = link,
                display_text = display_text,
                other = other
            )
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