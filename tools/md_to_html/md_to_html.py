from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.file_utils import get_meta_data
from tools.utils.logger_utils import get_logger
from tools.utils.mimetype_utils import MimeType
from tools.utils.pandoc_utils import pandoc_convert_text
from tools.utils.param_utils import get_md_text


class MarkdownToHtmlTool(Tool):
    logger = get_logger(__name__)

    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """
        # get parameters
        md_text = get_md_text(tool_parameters)

        try:
            result_file_bytes = pandoc_convert_text(md_text, "html5")
            yield self.create_blob_message(
                blob=result_file_bytes,
                meta=get_meta_data(
                    mime_type=MimeType.HTML,
                    output_filename=tool_parameters.get("output_filename"),
                ),
            )
        except Exception as e:
            self.logger.exception("Failed to convert file")
            yield self.create_text_message(f"Failed to convert markdown text to HTML file, error: {str(e)}")
            raise e
