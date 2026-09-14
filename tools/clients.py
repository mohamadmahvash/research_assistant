import requests
from core.exceptions import ExternalServiceError


class GithubClient:
    BASE_URL = "https://api.github.com"

    def search_repositories(self, query):
        try:
            response = requests.get(
                f"{self.BASE_URL}/search/repositories",
                params={
                    "q": query,
                    "sort": "stars",
                    "order": "desc",
                    "per_page": 10,
                },
                timeout=10,
            )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            raise ExternalServiceError("Github request timeout")

        except requests.exceptions.RequestException as e:
            raise ExternalServiceError(str(e))
