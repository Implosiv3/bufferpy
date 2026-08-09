from bufferpy.inputs.platforms.facebook.posts import FacebookPostMedatadaInput, FacebookReelMedatadaInput, FacebookStoryMedatadaInput
from bufferpy.inputs.platforms.instagram.posts import InstagramPostMetadataInput, InstagramReelMetadataInput, InstagramStoryMetadataInput
from bufferpy.inputs.platforms.instagram.reminders import InstagramPostReminderMetadataInput, InstagramReelReminderMetadataInput, InstagramStoryReminderMetadataInput
from bufferpy.inputs.platforms.tiktok.reminders import TiktokReelReminderMetadataInput
from bufferpy.inputs.platforms.tiktok.posts import TiktokReelMetadataInput
from bufferpy.enums import SchedulingType, ShareMode
from bufferpy.graphql.types import _GraphQLInput
from dataclasses import dataclass, field
from datetime import datetime
from typing import Union



@dataclass(slots = True)
class CreatePostInput(
    _GraphQLInput
):
    __graphql_field_map__ = {
        'channel_id': 'channelId',
        'due_at': 'dueAt',
        'scheduling_type': 'schedulingType',
    }

    channel_id: str
    text: str = ''
    assets: list[_GraphQLInput] = field(default_factory = list)
    mode: ShareMode = ShareMode.CUSTOM_SCHEDULED
    metadata: Union[InstagramPostMetadataInput, InstagramReelMetadataInput, InstagramStoryMetadataInput, FacebookPostMedatadaInput, FacebookReelMedatadaInput, FacebookStoryMedatadaInput, TiktokReelMetadataInput, TiktokReelReminderMetadataInput, InstagramPostReminderMetadataInput, InstagramReelReminderMetadataInput, InstagramStoryReminderMetadataInput, None] = None
    scheduling_type: SchedulingType = SchedulingType.AUTOMATIC
    due_at: Union[datetime, None] = None

