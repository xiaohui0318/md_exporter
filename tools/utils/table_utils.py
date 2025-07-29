from io import StringIO
from logging import Logger

import markdown
import pandas as pd
from pandas import DataFrame

from tools.utils.md_utils import MarkdownUtils


class TableParser:
    @staticmethod
    def parse_md_to_tables(logger: Logger, md_text: str, force_to_str: bool = True) -> list[pd.DataFrame]:
        """
        Parse markdown text to tables
        :param logger: Logger
        :param md_text: markdown text
        :param force_to_str: whether to force all columns to string type
        :return: list of tables
        """
        try:
            md_text = MarkdownUtils.strip_markdown_wrapper(md_text)
            html_str = markdown.markdown(text=md_text, extensions=['tables'])
            tables: list[DataFrame] = pd.read_html(StringIO(html_str))

            def post_process_table(table: DataFrame) -> DataFrame:
                table = table.fillna("")
                if force_to_str:
                    for col in table.columns:
                        if table[col].dtype != 'object':
                            table[col] = table[col].astype(str)
                return table

            tables = [post_process_table(table) for table in tables if not table.empty]

            if not tables or len(tables) <= 0:
                raise ValueError("No available tables parsed from markdown text")
            return tables
        except Exception as e:
            msg = f"Failed to parse markdown to tables, exception: {str(e)}"
            logger.exception(msg)
            raise ValueError(msg)
