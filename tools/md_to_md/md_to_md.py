from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.mimetype_utils import MimeType


class MarkdownToMarkdownFile(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """

        # get parameters
        md_text = tool_parameters.get("md_text")
        if not md_text:
            raise ValueError("Invalid input md_text")

        result_file_bytes = md_text.encode("utf-8")

        # yield self.create_text_message("The Markdown file is saved."),
        yield self.create_blob_message(
            blob=result_file_bytes,
            meta={"mime_type": MimeType.MD},
        )
        return
