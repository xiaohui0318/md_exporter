from typing import Any


def get_md_text(tool_parameters: dict[str, Any]) -> str:
    md_text = tool_parameters.get("md_text")
    if not md_text:
        raise ValueError("Empty input md_text")
    return md_text
