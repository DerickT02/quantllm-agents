# Renamed from `types.py` to avoid shadowing the Python stdlib `types` module.
# Keep small, shared TypedDicts and type helpers here.

from typing import TypedDict


# Example placeholder - add your project TypedDicts below
class ExampleConfig(TypedDict):
    name: str
    value: int
