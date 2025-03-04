import logging
from io import StringIO
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Generator

import markdown
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.mimetype_utils import MimeType


class MarkdownToXlsxFile(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """
        import pandas as pd

        # get parameters
        md_text = tool_parameters.get("md_text")
        if not md_text:
            raise ValueError("Invalid input md_text")

        # parse markdown to tables
        try:
            html_str = markdown.markdown(text=md_text, extensions=['tables'])
            tables = pd.read_html(StringIO(html_str))
        except Exception:
            logging.exception("Failed to parse markdown to tables")
            raise ValueError("Failed to parse markdown to tables.")

        # generate XLSX file
        try:
            with NamedTemporaryFile(suffix=".xlsx", delete=True) as temp_xlsx_file:
                with pd.ExcelWriter(temp_xlsx_file) as writer:
                    for i, table in enumerate(tables):
                        table.to_excel(writer, sheet_name=f"Sheet {i + 1}", index=False)
                result_file_bytes = Path(temp_xlsx_file.name).read_bytes()

        except Exception as e:
            logging.exception("Failed to convert file")
            yield self.create_text_message(
                f"Failed to convert markdown text to XLSX file, error: {str(e)}, html_str: {html_str}")
            return

        yield self.create_blob_message(blob=result_file_bytes, meta={
            "mime_type": MimeType.XLSX})
        return
