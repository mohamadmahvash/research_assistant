import requests
from bs4 import BeautifulSoup

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


class BooksClient:
    BASE_URL = "https://books.toscrape.com"

    def clean_query(self, query):

        stop_words = [
            "find",
            "a",
            "book",
            "that",
            "name",
            "is",
            "the",
        ]

        words = query.lower().split()

        return [
            word
            for word in words
            if word not in stop_words
        ]

    def parse_books(self, html, query):

        soup = BeautifulSoup(html,"lxml")

        keywords = self.clean_query(query)
        results = []

        for item in soup.select(
                "article.product_pod"
        ):

            title = item.h3.a["title"]

            title_lower = title.lower()

            if keywords and not all(
                    word in title_lower
                    for word in keywords
            ):
                continue

            results.append(
                {
                    "title": title,
                    "price": item.select_one(
                        ".price_color"
                    ).text,
                    "rating": item.p["class"][1],
                }
            )

        return results

    def search_books(self, query):
        try:
            response = requests.get(
                self.BASE_URL,
                timeout=10
            )
            response.raise_for_status()
            return self.parse_books(response.text, query)

        except requests.exceptions.RequestException as e:
            raise ExternalServiceError(
                str(e)
            )
