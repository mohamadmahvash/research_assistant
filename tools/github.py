from core.models import BaseResearchTool


class GithubTool(BaseResearchTool):
    name = "github"

    def can_handle(self, query: str) -> bool:
        keywords = [
            "github",
            "repository",
            "repositories",
            "repo",
            "repos",
            "ریپازیتوری",
            "ریپو"
        ]
        query = query.lower()
        return any(keyword in query for keyword in keywords)

    def execute(self, query):
        return {
            "tool": self.name,
            "query": query,
            "results": []
        }
