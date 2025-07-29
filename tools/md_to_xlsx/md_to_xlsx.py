from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Generator

import pandas as pd
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.file_utils import get_meta_data
from tools.utils.logger_utils import get_logger
from tools.utils.mimetype_utils import MimeType
from tools.utils.param_utils import get_md_text
from tools.utils.table_utils import TableParser


class MarkdownToXlsxTool(Tool):
    logger = get_logger(__name__)

    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """

        # get parameters
        md_text = get_md_text(tool_parameters)

        # parse markdown to tables
        tables = TableParser.parse_md_to_tables(self.logger, md_text)

        # generate XLSX file
        try:
            with NamedTemporaryFile(suffix=".xlsx", delete=True) as temp_xlsx_file:
                with pd.ExcelWriter(temp_xlsx_file) as writer:
                    for i, table in enumerate(tables):
                        sheet_name = f"Sheet{i + 1}"
                        table.to_excel(writer, sheet_name=sheet_name, index=False, na_rep='')
                        writer.sheets[sheet_name].autofit(max_width=200)

                result_file_bytes = Path(temp_xlsx_file.name).read_bytes()

            yield self.create_blob_message(
                blob=result_file_bytes,
                meta=get_meta_data(
                    mime_type=MimeType.XLSX,
                    output_filename=tool_parameters.get("output_filename"),
                ),
            )
        except Exception as e:
            self.logger.exception("Failed to convert file")
            yield self.create_text_message(
                f"Failed to convert markdown text to XLSX file, error: {str(e)}")
            return
