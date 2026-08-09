from dataclasses import dataclass
from datetime import datetime, timezone


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
    

