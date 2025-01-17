import logging
import os.path
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class MarkdownToPptxFile(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """

        # get parameters
        md_text = tool_parameters.get("md_text")
        if not md_text:
            raise ValueError("Invalid input md_text")

        try:
            # convert markdown text to pptx file
            current_script_folder = os.path.split(os.path.realpath(__file__))[0]
            with NamedTemporaryFile(suffix=".md", delete=True) as temp_md_file:
                temp_md_file.write(md_text.encode("utf-8"))
                with NamedTemporaryFile(suffix=".pptx", delete=True) as temp_pptx_file:
                    cmd = f"{current_script_folder}/md2pptx-5.2.2/md2pptx {Path(temp_md_file.name)} {Path(temp_pptx_file.name)}"
                    print(f"cmd: {cmd}")
                    os.system(cmd)
                    result_file_bytes = Path(temp_pptx_file.name).read_bytes()

        except Exception as e:
            logging.exception("Failed to convert file")
            yield self.create_text_message(f"Failed to convert markdown text to PDF file, error: {str(e)}")
            return

        # yield self.create_text_message("The PPTX file is saved.")
        yield self.create_blob_message(blob=result_file_bytes, meta={"mime_type": "application/pdf"})
        return
