import re
from typing import Generator

import httpx
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.mimetype_utils import MimeType
from tools.utils.param_utils import get_md_text


class MarkdownToLinkedImageTool(Tool):
    markdown_image_pattern = re.compile(r"!\[.*?]\(.*?\)")

    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """

        # get parameters
        md_text = get_md_text(tool_parameters)

        # extract code blocks
        image_urls = self.extract_image_urls(md_text)

        for url in image_urls:
            try:
                response = httpx.get(url, timeout=120)
                if response.status_code != 200:
                    yield self.create_text_message(f"Failed to download image from URL: {url},"
                                                   f" HTTP status code: {response.status_code}")
                    continue
                yield self.create_blob_message(
                    blob=response.content,
                    meta={"mime_type": response.headers['Content-Type'] or MimeType.PNG}
                )
            except:
                yield self.create_text_message(f"Failed to download image from URL: {url}")
                continue

    def extract_image_urls(self, markdown_text: str) -> list[str]:
        urls: list[str] = []
        match_image_tags = re.findall(self.markdown_image_pattern, markdown_text)

        for img in match_image_tags:
            # => ![](xxx.png)
            # <= xxx.png
            url = re.findall(r"\((.*?)\)", img)[0]
            if not url or not url.lower().startswith("http"):
                continue
            else:
                urls.append(url)

        return urls
