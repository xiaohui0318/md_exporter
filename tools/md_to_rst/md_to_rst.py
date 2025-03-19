import logging
from typing import Generator

import mistune
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from mistune.renderers.rst import RSTRenderer

from tools.utils.mimetype_utils import MimeType


class MarkdownToRstTool(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """

        # get parameters
        md_text = tool_parameters.get("md_text")
        if not md_text:
            raise ValueError("Invalid input md_text")

        try:
            convert_rst = mistune.create_markdown(renderer=RSTRenderer())
            rst_str = convert_rst(md_text)
            result_file_bytes = rst_str.encode("utf-8")
        except Exception as e:
            logging.exception("Failed to convert to RST file")
            yield self.create_text_message(f"Failed to convert markdown text to RST file, error: {str(e)}")
            return

        yield self.create_blob_message(
            blob=result_file_bytes,
            meta={"mime_type": MimeType.RST},
        )
        return
