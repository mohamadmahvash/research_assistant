from .clients import GithubClient
from core.models import BaseResearchTool


class GithubTool(BaseResearchTool):
    name = "github"

    def __init__(self):
        self.client = GithubClient()

    def can_handle(self, query: str):
        keywords = [
            "github",
            "repo",
            "repository",
            "project",
            "library",
            "package",
            "گیت هاب",
            "ریپو",
            "ریپوزیتوری",
            "پکیج",
            "گیت",
        ]
        query = query.lower()

        return any(
            keyword in query
            for keyword in keywords
        )

    def execute(self, query: str):
        data = self.client.search_repositories(query)
        repositories = []
        for item in data["items"]:
            repositories.append(
                {
                    "name": item["full_name"],
                    "url": item["html_url"],
                    "description": item["description"],
                    "stars": item["stargazers_count"],
                }
            )
        return repositories
