"""
TODO: The stickers will not be published,
they are just for the reminders that will
show a notification on your phone to go to
the app and copy the content to publish it
easier.
"""
from bufferpy.client.instagram import _Instagram
from bufferpy.client.facebook import _Facebook
from bufferpy.client.tiktok import _Tiktok
from bufferpy.exceptions import BufferException, ValidationError
from bufferpy.graphql import GraphQLClient
from bufferpy.models import Channel, Organization, Post, Account
# TODO: This below will be removed soon
from bufferpy.inputs import CreatePostInput, FacebookPostMedatadaInput, TiktokPostMedatadaInput
from bufferpy.inputs.assets import VideoAssetInput
from bufferpy.enums import PostType, ShareMode, SchedulingType
from bufferpy.queries import get_account_query, get_channels_query, create_post_mutation
from datetime import datetime, timezone
from typing import Any


"""
TODO: Te less requests we do, the less credits
we need, so please optimize it as much as you
can.
"""
class BufferClient:

    def __init__(
        self,
        api_key: str,
        timeout: int = 30,
    ) -> None:
        self._graphql = GraphQLClient(
            api_key = api_key,
            timeout = timeout,
        )

        # TODO: Do this only if 'instagram_channel_id' is provided
        self.instagram: _Instagram = _Instagram(self)
        """
        Shortcut to the functionality related to the
        Instagram channel.
        """
        self.facebook: _Facebook = _Facebook(self)
        """
        Shortcut to the functionality related to the
        Facebook channel.
        """
        self.tiktok: _Tiktok = _Tiktok(self)
        """
        Shortcut to the functionality related to the
        Tiktok channel.
        """


    def get_account(
        self
    ) -> Account:
        """
        Perform a query to obtain the account.
        """
        data = self._graphql.execute(
            get_account_query()
        )

        viewer = data['viewer']

        return Account(
            id = viewer['id'],
            name = viewer['name'],
            email = viewer['email'],
        )


    def get_organizations(
        self
    ) -> list[Organization]:
        """
        Perform a query to obtain the organizations 
        of the account logged in.
        """
        data = self._graphql.execute(
            get_account_query(),
        )

        return [
            Organization(
                id = item['id'],
                name = item['name'],
                owner_email = item['ownerEmail'],
            )
            for item in data['account']['organizations']
        ]


    def get_channels(
        self,
        organization_id: str,
    ) -> list[Channel]:
        """
        Perform a query to obtain the channels that
        are linked to the organization with the
        `organization_id` provided.
        """
        data = self._graphql.execute(
            get_channels_query(
                organization_id,
            )
        )

        return [
            Channel(
                id = item['id'],
                name = item['name'],
                service = item['service'],
            )
            for item in data['channels']
        ]


    def _schedule_post(
        self,
        input_data: CreatePostInput,
    ) -> Post:
        """
        *For internal use only*

        Common method to receive a creating post
        query that will be unwrapped and sent to
        the API to create it, returning the
        `Post` instance that has been created.
        """
        query = create_post_mutation(
            input_data,
        )

        data = self._graphql.execute(query)

        result = self._unwrap_mutation(
            data['createPost'],
        )

        return self._build_post(
            result['post'],
        )




    # TODO: Refactor with the other ones
    def create_scheduled_facebook_reel(
        self,
        channel_id: str,
        video_url: str,
        text: str,
        title: str,
        # date below
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        # publish_at: Union[datetime, None] = None,
    ) -> Post:
        """
        The date is UTC +00.00, MY is +08.00
        """
        scheduling_type = SchedulingType.AUTOMATIC
        # mode = (
        #     ShareMode.CUSTOM_SCHEDULED
        #     if publish_at is not None
        #     else ShareMode.SHARE_NOW
        # )
        # TODO: Make it work also for 'Publish now'
        mode = ShareMode.CUSTOM_SCHEDULED

        publish_at = datetime(
            year,
            month,
            day,
            hour,
            minute,
            tzinfo = timezone.utc,
        )

        metadata = FacebookPostMedatadaInput(
            type = PostType.REEL,
            # TODO: 'title' is not accepted
            # title = title,
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

        query = create_post_mutation(
            input_data,
        )

        data = self._graphql.execute(query)

        result = self._unwrap_mutation(
            data['createPost'],
        )

        return self._build_post(
            result['post'],
        )

    # TODO: Refactor with the other ones
    def create_scheduled_tiktok_post(
        self,
        channel_id: str,
        video_url: str,
        text: str,
        # TODO: 'title' is only valid if images, not video
        # title: str,
        # date below
        is_ai_generated: bool,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        # publish_at: Union[datetime, None] = None,
    ) -> Post:
        """
        The date is UTC +00.00, MY is +08.00
        """
        scheduling_type = SchedulingType.AUTOMATIC
        # mode = (
        #     ShareMode.CUSTOM_SCHEDULED
        #     if publish_at is not None
        #     else ShareMode.SHARE_NOW
        # )
        # TODO: Make it work also for 'Publish now'
        mode = ShareMode.CUSTOM_SCHEDULED

        publish_at = datetime(
            year,
            month,
            day,
            hour,
            minute,
            tzinfo = timezone.utc,
        )

        metadata = TiktokPostMedatadaInput(
            is_ai_generated = is_ai_generated
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

        query = create_post_mutation(
            input_data,
        )

        data = self._graphql.execute(query)

        result = self._unwrap_mutation(
            data['createPost'],
        )

        return self._build_post(
            result['post'],
        )

    def _unwrap_mutation(
        self,
        result: dict[str, Any],
    ) -> dict[str, Any]:
        typename = result['__typename']

        if typename.endswith('Error'):
            raise ValidationError(
                result.get('message', 'Unknown error')
            )

        return result

    def _build_post(
        self,
        data: dict[str, Any]
    ) -> Post:
        return Post(
            id = data['id'],
            channel_id = data['channel']['id'],
            text = data['text'],
            status = data['status'],
            publish_at = (
                datetime.fromisoformat(
                    data['dueAt'].replace('Z', '+00:00')
                )
                if data.get('dueAt')
                else None
            ),
            # publish_at = (
            #     datetime.fromisoformat(data["dueAt"])
            #     if data.get("dueAt")
            #     else None
            # ),
        )


