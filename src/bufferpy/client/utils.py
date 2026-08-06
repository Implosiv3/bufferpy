from datetime import datetime, timezone


def build_datetime(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int,
):
    """
    Build the datetime with the format expected,
    which is ISO 8601 format (UTC)
    """
    return datetime(
        year,
        month,
        day,
        hour,
        minute,
        tzinfo = timezone.utc,
    )