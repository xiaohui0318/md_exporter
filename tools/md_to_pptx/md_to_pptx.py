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

        # prepend template name
        # the default template name is "Martin Template.pptx" in "md2pptx-*" subfolder
        ppt_template_name = "template: Martin Template.pptx"
        if not md_text.startswith(ppt_template_name):
            md_text = ppt_template_name + "\n" + md_text
        md_text = "removeFirstSlide: yes\n" + md_text

        try:
            # write markdown text to a temp source file
            with NamedTemporaryFile(suffix=".md", delete=True) as temp_md_file:
                Path(temp_md_file.name).write_text(md_text, encoding="utf-8")

                # run md2pptx to convert md file to pptx file
                with NamedTemporaryFile(suffix=".pptx", delete=True) as temp_pptx_file:
                    current_script_folder = os.path.split(os.path.realpath(__file__))[0]
                    cmd = f"{current_script_folder}/md2pptx-5.4.1/md2pptx {Path(temp_md_file.name)} {Path(temp_pptx_file.name)}"
                    print(f"command: {cmd}")
                    os.system(cmd)
                    result_file_bytes = Path(temp_pptx_file.name).read_bytes()

        except Exception as e:
            logging.exception("Failed to convert file")
            yield self.create_text_message(f"Failed to convert markdown text to PDF file, error: {str(e)}")
            return

        # yield self.create_text_message("The PPTX file is saved.")
        yield self.create_blob_message(blob=result_file_bytes, meta={
            "mime_type": "application/vnd.openxmlformats-officedocument.presentationml.presentation"})
        return
