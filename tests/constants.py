"""
Modify this date to be in the future so you
can schedule the posts or notifications. You
have to provide a UTC+00.00 time.
"""
from bufferpy.inputs.dataclasses import PublicationDate


# Y, M, D, m, s
DATE = PublicationDate(
    year = 2026,
    month = 8,
    day = 6,
    hour = 17,
    minute = 50
)