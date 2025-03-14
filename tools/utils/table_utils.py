import logging
from io import StringIO

import markdown
import pandas as pd


class TableParser:
    @staticmethod
    def parse_md_to_tables(md_text: str) -> list[pd.DataFrame]:
        """
        Parse markdown text to tables
        :param md_text: markdown text
        :return: list of tables
        """
        try:
            html_str = markdown.markdown(text=md_text, extensions=['tables'])
            tables = pd.read_html(StringIO(html_str))
            if not tables or len(tables) < 1:
                raise ValueError("No available tables parsed from markdown text")
            return tables
        except Exception as e:
            msg = "Failed to parse markdown to tables"
            logging.exception(msg)
            raise ValueError(f"{msg}, exception: {str(e)}")
