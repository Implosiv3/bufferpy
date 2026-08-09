from tests.constants import DATE

import pytest


@pytest.mark.additional
def test_schedule_instagram_reel_post():
    from bufferpy.client.buffer import BufferClient
    from env_easy import Environment

    API_KEY = Environment.load_variable('BUFFER_API_KEY')
    INSTAGRAM_CHANNEL_ID = Environment.load_variable('INSTAGRAM_CHANNEL_ID')
    VIDEO_ASSET_DIRECT_LINK = Environment.load_variable('VIDEO_ASSET_DIRECT_LINK')

    client = BufferClient(API_KEY)

    # Post scheduled
    post = client.instagram.schedule_reel_post(
        channel_id = INSTAGRAM_CHANNEL_ID,
        video_url = VIDEO_ASSET_DIRECT_LINK,
        text = 'Automated post from bufferpy python library 🚀',
        publish_at = DATE,
        # metadata
        do_share_to_feed = True,
        is_ai_generated = True,
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
    )

    print(post)

    # Post now
    post = client.instagram.schedule_reel_post(
        channel_id = INSTAGRAM_CHANNEL_ID,
        video_url = VIDEO_ASSET_DIRECT_LINK,
        text = 'Automated post from bufferpy python library 🚀',
        publish_at = None,
        # metadata
        do_share_to_feed = True,
        is_ai_generated = True,
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
    )

    print(post)

    assert False


@pytest.mark.additional
def test_schedule_instagram_reel_notification():
    from bufferpy.client.buffer import BufferClient
    from env_easy import Environment

    API_KEY = Environment.load_variable('BUFFER_API_KEY')
    INSTAGRAM_CHANNEL_ID = Environment.load_variable('INSTAGRAM_CHANNEL_ID')
    VIDEO_ASSET_DIRECT_LINK = Environment.load_variable('VIDEO_ASSET_DIRECT_LINK')

    client = BufferClient(API_KEY)

    # Post scheduled
    post = client.instagram.schedule_reel_notification(
        channel_id = INSTAGRAM_CHANNEL_ID,
        video_url = VIDEO_ASSET_DIRECT_LINK,
        text = 'Automated post from bufferpy python library 🚀',
        publish_at = DATE,
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
        music = 'Music ok',
        display_text = 'Something to be displayed',
        topics = 'topics, how',
        products = 'products, how'
    )

    print(post)

    # Post now
    post = client.instagram.schedule_reel_notification(
        channel_id = INSTAGRAM_CHANNEL_ID,
        video_url = VIDEO_ASSET_DIRECT_LINK,
        text = 'Automated post from bufferpy python library 🚀',
        publish_at = None,
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
        music = 'Music ok',
        display_text = 'Something to be displayed',
        topics = 'topics, how',
        products = 'products, how'
    )

    print(post)

    assert False


# TODO: Test with more than 1 image
@pytest.mark.additional
def test_schedule_instagram_post_post():
    from bufferpy.client.buffer import BufferClient
    from env_easy import Environment

    API_KEY = Environment.load_variable('BUFFER_API_KEY')
    INSTAGRAM_CHANNEL_ID = Environment.load_variable('INSTAGRAM_CHANNEL_ID')
    IMAGE_ASSET_DIRECT_LINK = Environment.load_variable('IMAGE_ASSET_DIRECT_LINK')

    client = BufferClient(API_KEY)

    # Post scheduled
    post = client.instagram.schedule_post_post(
        channel_id = INSTAGRAM_CHANNEL_ID,
        image_url = IMAGE_ASSET_DIRECT_LINK,
        text = 'Automated post from bufferpy python library 🚀',
        publish_at = DATE,
        # metadata
        is_ai_generated = True,
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
    )

    print(post)

    # Post now
    post = client.instagram.schedule_post_post(
        channel_id = INSTAGRAM_CHANNEL_ID,
        image_url = IMAGE_ASSET_DIRECT_LINK,
        text = 'Automated post from bufferpy python library 🚀',
        publish_at = None,
        # metadata
        is_ai_generated = True,
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
    )

    print(post)

    assert False


# TODO: Test with more than 1 image
@pytest.mark.additional
def test_schedule_instagram_post_notification():
    from bufferpy.client.buffer import BufferClient
    from env_easy import Environment

    API_KEY = Environment.load_variable('BUFFER_API_KEY')
    INSTAGRAM_CHANNEL_ID = Environment.load_variable('INSTAGRAM_CHANNEL_ID')
    IMAGE_ASSET_DIRECT_LINK = Environment.load_variable('IMAGE_ASSET_DIRECT_LINK')

    client = BufferClient(API_KEY)

    # Post scheduled
    post = client.instagram.schedule_post_notification(
        channel_id = INSTAGRAM_CHANNEL_ID,
        image_url = IMAGE_ASSET_DIRECT_LINK,
        text = 'Automated post from bufferpy python library 🚀',
        publish_at = DATE,
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
        music = 'Music ok',
        # display_text = 'Something to be displayed',
        # topics = 'topics, how',
        products = 'products, how'
    )

    print(post)

    # Post now
    post = client.instagram.schedule_post_notification(
        channel_id = INSTAGRAM_CHANNEL_ID,
        image_url = IMAGE_ASSET_DIRECT_LINK,
        text = 'Automated post from bufferpy python library 🚀',
        publish_at = None,
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
        music = 'Music ok',
        # display_text = 'Something to be displayed',
        # topics = 'topics, how',
        products = 'products, how'
    )

    print(post)

    assert False


# TODO: Test with more than 1 image
@pytest.mark.additional
def test_schedule_instagram_story_post():
    from bufferpy.client.buffer import BufferClient
    from env_easy import Environment

    API_KEY = Environment.load_variable('BUFFER_API_KEY')
    INSTAGRAM_CHANNEL_ID = Environment.load_variable('INSTAGRAM_CHANNEL_ID')
    IMAGE_ASSET_DIRECT_LINK = Environment.load_variable('IMAGE_ASSET_DIRECT_LINK')
    VIDEO_ASSET_DIRECT_LINK = Environment.load_variable('VIDEO_ASSET_DIRECT_LINK')

    client = BufferClient(API_KEY)

    # Post scheduled
    post = client.instagram.schedule_story_post(
        channel_id = INSTAGRAM_CHANNEL_ID,
        image_url = IMAGE_ASSET_DIRECT_LINK,
        text = 'Automated post from bufferpy python library 🚀',
        publish_at = DATE,
        # metadata
        is_ai_generated = True,
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
    )

    print(post)

    # Post now
    post = client.instagram.schedule_story_post(
        channel_id = INSTAGRAM_CHANNEL_ID,
        image_url = IMAGE_ASSET_DIRECT_LINK,
        text = 'Automated post from bufferpy python library 🚀',
        publish_at = None,
        # metadata
        is_ai_generated = True,
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
    )

    print(post)

    assert False


# TODO: Test with more than 1 image
@pytest.mark.additional
def test_schedule_instagram_story_notification():
    from bufferpy.client.buffer import BufferClient
    from env_easy import Environment

    API_KEY = Environment.load_variable('BUFFER_API_KEY')
    INSTAGRAM_CHANNEL_ID = Environment.load_variable('INSTAGRAM_CHANNEL_ID')
    IMAGE_ASSET_DIRECT_LINK = Environment.load_variable('IMAGE_ASSET_DIRECT_LINK')

    client = BufferClient(API_KEY)

    # Post scheduled
    post = client.instagram.schedule_story_notification(
        channel_id = INSTAGRAM_CHANNEL_ID,
        image_url = IMAGE_ASSET_DIRECT_LINK,
        text = 'Automated post from bufferpy python library 🚀',
        publish_at = DATE,
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
        music = 'Music ok',
        link = 'Link ok',
        display_text = 'Something to be displayed',
        other = 'Other, how'
    )

    print(post)

    # Post now
    post = client.instagram.schedule_story_notification(
        channel_id = INSTAGRAM_CHANNEL_ID,
        image_url = IMAGE_ASSET_DIRECT_LINK,
        text = 'Automated post from bufferpy python library 🚀',
        publish_at = None,
        # TODO: Paid plan required
        # first_comment = 'Hola, testing',
        music = 'Music ok',
        link = 'Link ok',
        display_text = 'Something to be displayed',
        other = 'Other, how'
    )

    print(post)

    assert False