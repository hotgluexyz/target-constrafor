"""Constrafor target class."""

from typing import Type
from singer_sdk import typing as th
from singer_sdk.sinks import Sink
from target_hotglue.target import TargetHotglue

from target_constrafor.sinks import FallbackSink


class TargetConstrafor(TargetHotglue):
    """Sample target for Constrafor."""

    name = "target-constrafor"

    config_jsonschema = th.PropertiesList(
        th.Property("access_token", th.StringType, required=True),
    ).to_dict()

    SINK_TYPES = [FallbackSink]

    def get_sink_class(self, stream_name: str) -> Type[Sink]:
        """Get sink for a stream."""
        return FallbackSink


if __name__ == "__main__":
    TargetConstrafor.cli()
