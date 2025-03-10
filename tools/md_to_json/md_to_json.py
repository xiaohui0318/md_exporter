import logging
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.mimetype_utils import MimeType
from tools.utils.table_utils import TableParser


class MarkdownToJsonFile(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """

        # get parameters
        md_text = tool_parameters.get("md_text")
        if not md_text:
            raise ValueError("Invalid input md_text")

        # parse markdown to tables
        tables = TableParser.parse_md_to_tables(md_text)

        # generate JSON file
        try:
            table = tables[0]
            with NamedTemporaryFile(suffix=".json", delete=True) as temp_json_file:
                table.to_json(temp_json_file, index=False, orient='records')
                result_file_bytes = Path(temp_json_file.name).read_bytes()

        except Exception as e:
            logging.exception("Failed to convert to JSON file")
            yield self.create_text_message(f"Failed to convert markdown text to JSON file, error: {str(e)}")
            return

        yield self.create_blob_message(
            blob=result_file_bytes,
            meta={"mime_type": MimeType.JSON},
        )
        return
