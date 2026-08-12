from dataclasses import dataclass
from datetime import datetime, timezone


"""
TODO: This class should be avoided and use
datetime utc instead directly...
"""
@dataclass
class PublicationDate:
    """
    Dataclass to represent the datetime in which we
    want a post to be published.
    """
    
    year: int
    month: int
    day: int
    hour: int
    minute: int


    @classmethod
    def from_datetime(
        cls,
        value: datetime,
    ) -> 'PublicationDate':
        """
        Get a `PublicationDate` class instance with
        the datetime provided as `value`, that will
        be considered UTC.
        """
        value = value.astimezone(timezone.utc)

        return cls(
            year = value.year,
            month = value.month,
            day = value.day,
            hour = value.hour,
            minute = value.minute,
        )

    @property
    def as_iso8601(
        self
    ) -> datetime:
        """
        Build the datetime with the format expected
        by the Buffer API, which is ISO 8601 format
        (UTC).
        """
        return datetime(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            tzinfo = timezone.utc,
        )
    

