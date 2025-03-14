import logging
from typing import Generator

import markdown
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from lxml import html, etree

from tools.utils.mimetype_utils import MimeType


class MarkdownToXmlTool(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """

        # get parameters
        md_text = tool_parameters.get("md_text")
        if not md_text:
            raise ValueError("Invalid input md_text")

        try:
            html_str = markdown.markdown(text=md_text, extensions=["extra", "toc"])
            xml_element = html.fromstring(html_str)
            result_file_bytes = etree.tostring(xml_element, xml_declaration=True, pretty_print=True, encoding="UTF-8")
        except Exception as e:
            logging.exception("Failed to convert to XML file")
            yield self.create_text_message(f"Failed to convert markdown text to XML file, error: {str(e)}")
            return

        yield self.create_blob_message(
            blob=result_file_bytes,
            meta={"mime_type": MimeType.XML},
        )
        return
