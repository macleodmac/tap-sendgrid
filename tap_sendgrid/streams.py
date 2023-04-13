"""Stream type classes for tap-sendgrid."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_sendgrid.client import sendgridStream



class BouncesStream(sendgridStream):
    """Define custom stream."""

    name = "bounces"
    path = "/suppression/bounces"
    primary_keys = ["email", "created"]
    replication_key = "created"
    schema = th.PropertiesList(
        th.Property("created", th.IntegerType),
        th.Property("email", th.StringType),
        th.Property("reason", th.StringType),
            th.Property("status", th.StringType),
    ).to_dict()
 