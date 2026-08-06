"""
A simple library to connect with the Buffer
platform API and make it easier to schedule
your posts.

The buffer platform includes its own hierarchy:
- You own your account, linked to your email.
- The account has organizations, your brands.
- Each organization has channels, the platforms
in which you publish (Instagram, Tiktok, etc.).
"""
from bufferpy.client.buffer import BufferClient


__all__ = [
    'BufferClient',
]