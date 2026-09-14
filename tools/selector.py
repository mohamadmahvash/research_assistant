from .books import BooksTool
from .github import GithubTool


class ToolSelector:
    tools = [
        BooksTool(),
        GithubTool(),
    ]

    @classmethod
    def select(cls, query):

        for tool in cls.tools:
            if tool.can_handle(query):
                return tool

        return None
