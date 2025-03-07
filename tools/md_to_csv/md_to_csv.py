import logging
from io import StringIO
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Generator

import markdown
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.mimetype_utils import MimeType


class MarkdownToCsvFile(Tool):
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
            logging.exception("Failed to parse markdown to table")
            raise ValueError("Failed to parse markdown to table.")

        # generate CSV file
        try:
            with NamedTemporaryFile(suffix=".csv", delete=True) as temp_csv_file:
                with pd.ExcelWriter(temp_csv_file) as writer:
                    table = tables[0]
                    table.to_csv(writer, index=False)
                result_file_bytes = Path(temp_csv_file.name).read_bytes()

        except Exception as e:
            logging.exception("Failed to convert to CSV file")
            yield self.create_text_message(
                f"Failed to convert markdown text to CSV file, error: {str(e)}, html_str: {html_str}")
            return

        yield self.create_blob_message(blob=result_file_bytes, meta={"mime_type": MimeType.CSV})
        return
