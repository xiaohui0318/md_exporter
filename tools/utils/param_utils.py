import re
from typing import Any

from tools.utils.md_utils import MarkdownUtils


def get_md_text(tool_parameters: dict[str, Any],
                is_strip_wrapper: bool = False,
                is_remove_think_tag: bool = True,
                is_normalize_line_breaks: bool = True,
                ) -> str:
    md_text = tool_parameters.get("md_text")
    md_text = md_text.strip() if md_text else None
    if not md_text:
        raise ValueError("Empty input md_text")

    # remove think tag
    if is_remove_think_tag and "<think>" in md_text:
        think_tag_pattern = r'<think>.*?</think>'
        md_text = re.sub(think_tag_pattern, '', md_text, flags=re.DOTALL)

    if is_strip_wrapper:
        md_text = MarkdownUtils.strip_markdown_wrapper(md_text)

    # line breaks normalization by auto conversion from `\\n` to `\n`
    if is_normalize_line_breaks and "\\n" in md_text:
        md_text = md_text.replace("\\n", "\n")

    return md_text


def get_param_value(tool_parameters: dict[str, Any], param_name: str, default_value: Any = None) -> Any:
    param_value = tool_parameters.get(param_name, default_value)
    if not param_value:
        raise ValueError(f"Empty input {param_name}")

    return param_value
