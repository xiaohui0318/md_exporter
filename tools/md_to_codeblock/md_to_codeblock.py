import re
from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.mimetype_utils import MimeType


class MarkdownToCodeblockTool(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """

        # get parameters
        md_text = tool_parameters.get("md_text")
        if not md_text:
            raise ValueError("Invalid input md_text")

        code_blocks = self.extract_markdown_code_blocks(md_text)

        for code_block in code_blocks:
            lang_type = code_block.get("lang_type")
            content = code_block.get("content")

            if not content:
                continue
            else:
                result_file_bytes = content.encode("utf-8")

            mime_type = self.get_mime_type(lang_type)

            yield self.create_blob_message(
                blob=result_file_bytes,
                meta={"mime_type": mime_type},
            )

    @staticmethod
    def extract_markdown_code_blocks(text: str) -> list[dict[str:str]]:
        """
        从Markdown文本中提取所有代码块及其语言类型
        返回格式：[{"type": "语言名称", "content": "代码内容"}, ...]
        """
        code_blocks = []
        # 正则表达式模式（支持语言类型识别和多行代码）
        pattern = re.compile(r'```([a-zA-Z0-9\+#\-_]*)\s*\n(.*?)\n```', re.DOTALL)

        # 遍历所有匹配结果
        for match in pattern.finditer(text):
            lang_type = match.group(1).strip() or 'text'
            code_content = match.group(2).strip()

            code_blocks.append({
                "lang_type": lang_type,
                "content": code_content
            })

        return code_blocks

    @staticmethod
    def get_mime_type(lang_type: str) -> str:
        mime_types = {
            "css": MimeType.CSS,
            "csv": MimeType.CSV,
            "python": MimeType.PY,
            "json": MimeType.JSON,
            "javascript": MimeType.JS,
            "bash": MimeType.SH,
            "sh": MimeType.SH,
            "svg": MimeType.SVG,
            "xml": MimeType.XML,
            "html": MimeType.HTML,
            "markdown": MimeType.MD,
        }
        return mime_types.get(lang_type.lower(), MimeType.TXT)
