import os
from typing import Dict

from langchain.tools.base import BaseMultiArgTool


class WriteFileTool(BaseMultiArgTool):
    name: str = "write_file"
    tool_args: Dict[str, str] = {"file": "<file>", "text": "<text>"}
    description: str = "Write file to disk"

    def _run(self, file: str, text: str) -> str:
        try:
            directory = os.path.dirname(file)
            if not os.path.exists(directory) and directory:
                os.makedirs(directory)
            with open(file, "w", encoding="utf-8") as f:
                f.write(text)
            return "File written to successfully."
        except Exception as e:
            return "Error: " + str(e)

    async def _arun(self, tool_input: str) -> str:
        raise NotImplementedError
