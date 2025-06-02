from typing import final

from dify_plugin import Tool
from dify_plugin.core.runtime import Session
from dify_plugin.entities.tool import ToolRuntime


class CommonTool(Tool):
    def __init__(
            self,
            runtime: ToolRuntime,
            session: Session,
    ):
        super().__init__(runtime,session)