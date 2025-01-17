import logging
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from markdowntodocx import markdownconverter

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
            with NamedTemporaryFile(suffix=".docx", delete=True) as temp_docx_file:
                markdownconverter.markdownToWordFromString(string=md_text, outfile=temp_docx_file)
                result_file_bytes = Path(temp_docx_file.name).read_bytes()
        except Exception as e:
            logging.exception("Failed to convert file")
            yield self.create_text_message(f"Failed to convert markdown text to DOCX file, error: {str(e)}")
            return

        # yield self.create_text_message("The DOCX file is saved."),
        yield self.create_blob_message(
            blob=result_file_bytes,
            meta={"mime_type": MimeType.DOCX},
        )
        return
