from tests.constants import DATE

import pytest


@pytest.mark.additional
def test_schedule_tiktok_reel_post():
    from bufferpy.client.buffer import BufferClient
    from env_easy import Environment

    API_KEY = Environment.load_variable('BUFFER_API_KEY')
    TIKTOK_CHANNEL_ID = Environment.load_variable('TIKTOK_CHANNEL_ID')
    VIDEO_ASSET_DIRECT_LINK = Environment.load_variable('VIDEO_ASSET_DIRECT_LINK')

    client = BufferClient(API_KEY)

    post = client.tiktok.schedule_reel_post(
        channel_id = TIKTOK_CHANNEL_ID,
        video_url = VIDEO_ASSET_DIRECT_LINK,
        text = 'Automated post from buffer-api python library V2 🚀',
        # date
        year = DATE[0],
        month = DATE[1],
        day = DATE[2],
        hour = DATE[3],
        minute = DATE[4],
        # metadata
        is_ai_generated = True
    )

    print(post)

    assert False


@pytest.mark.additional
def test_schedule_tiktok_reel_notification():
    from bufferpy.client.buffer import BufferClient
    from env_easy import Environment

    API_KEY = Environment.load_variable('BUFFER_API_KEY')
    TIKTOK_CHANNEL_ID = Environment.load_variable('TIKTOK_CHANNEL_ID')
    VIDEO_ASSET_DIRECT_LINK = Environment.load_variable('VIDEO_ASSET_DIRECT_LINK')

    client = BufferClient(API_KEY)

    post = client.tiktok.schedule_reel_notification(
        channel_id = TIKTOK_CHANNEL_ID,
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