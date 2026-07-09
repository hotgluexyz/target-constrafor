"""Constrafor target class."""

from hotglue_singer_sdk import typing as th
from hotglue_singer_sdk.target_sdk.target import TargetHotglue

from target_constrafor.sinks import FallbackSink, InvoicesCommitmentsSink


class TargetConstrafor(TargetHotglue):
    """Sample target for Constrafor."""

    name = "target-constrafor"

    config_jsonschema = th.PropertiesList(
        th.Property("api_key", th.StringType, required=True),
    ).to_dict()

    SINK_TYPES = [InvoicesCommitmentsSink]
    default_sink_class = FallbackSink


if __name__ == "__main__":
    TargetConstrafor.cli()
