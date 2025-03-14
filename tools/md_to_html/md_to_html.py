import logging
from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.md_utils import MarkdownUtils
from tools.utils.mimetype_utils import MimeType


class MarkdownToHtmlTool(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """
        # get parameters
        md_text: str = tool_parameters.get("md_text")
        if not md_text:
            raise ValueError("Invalid input md_text")

        try:
            md_text = MarkdownUtils.strip_markdown_wrapper(md_text)
            html_str = MarkdownUtils.convert_markdown_to_html(md_text)
            result_file_bytes = html_str.encode("utf-8")
        except Exception as e:
            logging.exception("Failed to convert file")
            yield self.create_text_message(f"Failed to convert markdown text to HTML file, error: {str(e)}")
            return

        yield self.create_blob_message(
            blob=result_file_bytes,
            meta={"mime_type": MimeType.HTML},
        )
        return
