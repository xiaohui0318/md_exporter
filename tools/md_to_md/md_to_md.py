from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.mimetype_utils import MimeType
from tools.utils.param_utils import get_md_text


class MarkdownToMarkdownTool(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """

        # get parameters
        md_text = get_md_text(tool_parameters)
        result_file_bytes = md_text.encode("utf-8")

        yield self.create_blob_message(
            blob=result_file_bytes,
            meta={"mime_type": MimeType.MD},
        )
        return
