import logging
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.core.table_parser import parse_md_to_tables
from tools.utils.mimetype_utils import MimeType


class MarkdownToCsvFile(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """

        # get parameters
        md_text = tool_parameters.get("md_text")
        if not md_text:
            raise ValueError("Invalid input md_text")

        # parse markdown to tables
        tables = parse_md_to_tables(md_text)

        # generate CSV file
        try:
            table = tables[0]
            with NamedTemporaryFile(suffix=".csv", delete=True) as temp_csv_file:
                table.to_csv(temp_csv_file, index=False, encoding="utf-8")
                result_file_bytes = Path(temp_csv_file.name).read_bytes()

        except Exception as e:
            logging.exception("Failed to convert to CSV file")
            yield self.create_text_message(f"Failed to convert markdown text to CSV file, error: {str(e)}")
            return

        yield self.create_blob_message(
            blob=result_file_bytes,
            meta={"mime_type": MimeType.CSV},
        )
        return
