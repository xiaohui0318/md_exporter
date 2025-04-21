import logging
import re
from typing import Generator

import httpx
import markdown
from bs4 import BeautifulSoup
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

    def extract_image_urls(self, md_text: str) -> list[str]:
        html = markdown.markdown(text=md_text, extensions=["extra", "toc"])

        image_urls: list[str] = []
        try:
            soup = BeautifulSoup(html, 'html.parser')
            img_tags = soup.find_all('img')
            image_urls = [img.get('src') for img in img_tags if img.get('src')]
        except:
            logging.exception("Failed to extract image URLs from markdown text by html parser")

            match_image_tags = re.findall(self.markdown_image_pattern, md_text)
            for img in match_image_tags:
                # => ![](xxx.png)
                # <= xxx.png
                url = re.findall(r"\((.*?)\)", img)[0]
                image_urls.append(url)

        result_image_urls = []
        for url in image_urls:
            if not url or not url.lower().startswith("http"):
                continue
            elif url in result_image_urls:
                continue
            else:
                result_image_urls.append(url)

        return result_image_urls
