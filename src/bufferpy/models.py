from dataclasses import dataclass
from datetime import datetime
from typing import Union


@dataclass(slots = True, frozen = True)
class Account:
    """
    The account that is registered in the platform,
    that includes these fields:
    - `id`
    - `name`
    - `email`
    """

    id: str
    name: str
    email: str


@dataclass(slots = True, frozen = True)
class Organization:
    """
    One organization included in an account, that
    includes these fields:
    - `id`
    - `name`
    - `owner_email`
    """

    id: str
    name: str
    owner_email: str


@dataclass(slots = True, frozen = True)
class Channel:
    """
    One channel that belongs to an organization and
    includes these fields:
    - `id`
    - `name`
    - `service`

    The `service` will indicate the social platform
    that is linked, such as:
    - `instagram`
    - `facebook`
    - `tiktok`
    - `...`
    """

    id: str
    name: str
    service: str


@dataclass(slots = True, frozen = True)
class Asset:
    """
    An asset that will be included in a post, such
    as an image, a video, etc. It includes these
    fields:
    - `id`
    - `source`
    - `mime_type`
    - `type`

    TODO: Explain a bit the special ones
    """

    id: str
    source: Union[str, None] = None
    mime_type: Union[str, None] = None
    type: Union[str, None] = None


@dataclass(slots = True, frozen = True)
class Post:
    """
    A post, that belongs to a specific `Channel`,
    can include some `Assets`, and has these
    fields:
    - `id`
    - `channel_id`
    - `text`
    - `status`
    - `publish_at`

    TODO: Explain a bit the special ones
    """

    id: str
    channel_id: str
    text: str
    status: str
    publish_at: Union[datetime, None] = None