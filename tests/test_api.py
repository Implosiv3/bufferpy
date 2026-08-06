"""
Set the channel ids in your .env so you can
test it directly here.
"""
import pytest


@pytest.mark.additional
def test_get_organizations_and_channels():
    from bufferpy.client.buffer import BufferClient
    from env_easy import Environment

    API_KEY = Environment.load_variable('BUFFER_API_KEY')

    client = BufferClient(API_KEY)

    organizations = client.organizations()

    assert organizations is not None

    channels = client.channels(
        organization_id = organizations[0].id
    )

    assert channels is not None