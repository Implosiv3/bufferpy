"""
Tiktok reminders, which are notifications that
will be sent to your phone so you can manually
publish the post by yourself.

These reminders does not include any stickers
metadata.
"""
from bufferpy.inputs.platforms.tiktok.consts import PLATFORM
from bufferpy.inputs.platforms.base import _PlatformMetadataInput
from dataclasses import dataclass
from typing import ClassVar


# TODO: This is exactly as the post class
@dataclass(slots = True)
class TiktokReelReminderMetadataInput(
    _PlatformMetadataInput
):
    """
    Metadata for a Tiktok post that is a reel.
    """

    platform: ClassVar[str] = PLATFORM