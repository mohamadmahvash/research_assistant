import requests


class GithubClient:
    BASE_URL = "https://api.github.com"

    def search_repositories(self, query):
        response = requests.get(
            f"{self.BASE_URL}/search/repositories",
            params={
                "q": query,
                "sort": "stars",
                "order": "desc",
                "per_page": 10,
            },
            timeout=10
        )

        response.raise_for_status()
        return response.json()
