from tests.constants import DATE

import pytest


@pytest.mark.additional
def test_schedule_facebook_reel_post():
    from bufferpy.client.buffer import BufferClient
    from env_easy import Environment

    API_KEY = Environment.load_variable('BUFFER_API_KEY')
    FACEBOOK_CHANNEL_ID = Environment.load_variable('FACEBOOK_CHANNEL_ID')
    VIDEO_ASSET_DIRECT_LINK = Environment.load_variable('VIDEO_ASSET_DIRECT_LINK')

    client = BufferClient(API_KEY)

    post = client.facebook.schedule_reel_post(
        channel_id = FACEBOOK_CHANNEL_ID,
        video_url = VIDEO_ASSET_DIRECT_LINK,
        text = 'Automated post from buffer-api python library V2 🚀',
        # date
        year = DATE[0],
        month = DATE[1],
        day = DATE[2],
        hour = DATE[3],
        minute = DATE[4],
        # metadata
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
    )

    print(post)

    assert False


@pytest.mark.additional
def test_schedule_facebook_post_post():
    from bufferpy.client.buffer import BufferClient
    from env_easy import Environment

    API_KEY = Environment.load_variable('BUFFER_API_KEY')
    FACEBOOK_CHANNEL_ID = Environment.load_variable('FACEBOOK_CHANNEL_ID')
    VIDEO_ASSET_DIRECT_LINK = Environment.load_variable('VIDEO_ASSET_DIRECT_LINK')
    IMAGE_ASSET_DIRECT_LINK = Environment.load_variable('IMAGE_ASSET_DIRECT_LINK')

    client = BufferClient(API_KEY)

    post = client.facebook.schedule_post_post(
        channel_id = FACEBOOK_CHANNEL_ID,
        image_url = IMAGE_ASSET_DIRECT_LINK,
        text = 'Automated post from buffer-api python library V2 🚀',
        # date
        year = DATE[0],
        month = DATE[1],
        day = DATE[2],
        hour = DATE[3],
        minute = DATE[4],
        # metadata
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
    )

    print(post)

    assert False


@pytest.mark.additional
def test_schedule_facebook_story_post():
    from bufferpy.client.buffer import BufferClient
    from env_easy import Environment

    API_KEY = Environment.load_variable('BUFFER_API_KEY')
    FACEBOOK_CHANNEL_ID = Environment.load_variable('FACEBOOK_CHANNEL_ID')
    VIDEO_ASSET_DIRECT_LINK = Environment.load_variable('VIDEO_ASSET_DIRECT_LINK')
    IMAGE_ASSET_DIRECT_LINK = Environment.load_variable('IMAGE_ASSET_DIRECT_LINK')

    client = BufferClient(API_KEY)

    post = client.facebook.schedule_story_post(
        channel_id = FACEBOOK_CHANNEL_ID,
        image_url = IMAGE_ASSET_DIRECT_LINK,
        text = 'Automated post from buffer-api python library V2 🚀',
        # date
        year = DATE[0],
        month = DATE[1],
        day = DATE[2],
        hour = DATE[3],
        minute = DATE[4],
        # metadata
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
    )

    print(post)

    assert False