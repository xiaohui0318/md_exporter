from typing import Any

from tools.utils.md_utils import MarkdownUtils


def get_md_text(tool_parameters: dict[str, Any], is_strip_wrapper: bool = False) -> str:
    md_text = tool_parameters.get("md_text")
    if not md_text:
        raise ValueError("Empty input md_text")

    if is_strip_wrapper:
        md_text = MarkdownUtils.strip_markdown_wrapper(md_text)

    return md_text
