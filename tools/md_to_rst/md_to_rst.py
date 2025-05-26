import logging
from typing import Generator

import mistune
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from mistune.renderers.rst import RSTRenderer

from tools.utils.file_utils import get_meta_data
from tools.utils.logger_utils import get_logger
from tools.utils.mimetype_utils import MimeType
from tools.utils.param_utils import get_md_text


class MarkdownToRstTool(Tool):
    logger = get_logger(__name__)

    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """

        # get parameters
        md_text = get_md_text(tool_parameters)
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
            meta=get_meta_data(
                mime_type=MimeType.RST,
                output_filename=tool_parameters.get("output_filename"),
            ),
        )
        return
