import logging
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.mimetype_utils import MimeType
from tools.utils.table_utils import TableParser


class MarkdownToXlsxTool(Tool):
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
        tables = TableParser.parse_md_to_tables(md_text)

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
                f"Failed to convert markdown text to XLSX file, error: {str(e)}")
            return

        yield self.create_blob_message(
            blob=result_file_bytes,
            meta={"mime_type": MimeType.XLSX},
        )
        return
