"""sendgrid tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_sendgrid import streams


class Tapsendgrid(Tap):
    """sendgrid tap class."""

    name = "tap-sendgrid"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,
            description="The token to authenticate against the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.sendgridStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.BouncesStream(self),
        ]


if __name__ == "__main__":
    Tapsendgrid.cli()
