import logging
from typing import Generator

import markdown
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from html2docx import html2docx

from tools.utils.md_utils import MarkdownUtils
from tools.utils.mimetype_utils import MimeType


class MarkdownToDocxFile(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """
        # get parameters
        md_text = tool_parameters.get("md_text")
        if not md_text:
            raise ValueError("Invalid input md_text")

        try:
            md_text = MarkdownUtils.strip_markdown_wrapper(md_text)

            # Legacy: using markdowntodocx lib
            # with NamedTemporaryFile(suffix=".docx", delete=True) as temp_docx_file:
            #     markdownconverter.markdownToWordFromString(string=md_text, outfile=temp_docx_file)
            #     result_file_bytes = Path(temp_docx_file.name).read_bytes()

            extensions = ["extra", "toc"]
            html = markdown.markdown(text=md_text, extensions=extensions)
            output_buf = html2docx(html, title="My Document")
            result_file_bytes = output_buf.getvalue()
        except Exception as e:
            logging.exception("Failed to convert file")
            yield self.create_text_message(f"Failed to convert markdown text to DOCX file, error: {str(e)}")
            return

        yield self.create_blob_message(
            blob=result_file_bytes,
            meta={"mime_type": MimeType.DOCX},
        )
        return
