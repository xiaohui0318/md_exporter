import logging
from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.file_utils import get_meta_data
from tools.utils.mimetype_utils import MimeType
from tools.utils.pandoc_utils import pandoc_convert_file
from tools.utils.param_utils import get_md_text


class MarkdownToDocxTool(Tool):
    logger = logging.getLogger(__name__)

    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """
        # get parameters
        md_text = get_md_text(tool_parameters, is_strip_wrapper=True)
        try:
            result_file_bytes = pandoc_convert_file(md_text, "docx")
            yield self.create_blob_message(
                blob=result_file_bytes,
                meta=get_meta_data(
                    mime_type=MimeType.DOCX,
                    output_filename=tool_parameters.get("output_filename"),
                ),
            )
        except Exception as e:
            self.logger.exception("Failed to convert markdown text to DOCX file")
            yield self.create_text_message(f"Failed to convert markdown text to DOCX file, error: {str(e)}")
            raise e
