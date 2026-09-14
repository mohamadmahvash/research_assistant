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

    def parse_books(self, html, query):

        soup = BeautifulSoup(
            html,
            "lxml"
        )

        keywords = query.lower().split()

        matched_books = []
        all_books = []

        for item in soup.select(
                "article.product_pod"
        ):

            title = item.h3.a["title"]

            book = {
                "title": title,
                "price": item.select_one(
                    ".price_color"
                ).text,
                "rating": item.p["class"][1],
            }

            all_books.append(book)

            title_lower = title.lower()

            if any(
                    word in title_lower
                    for word in keywords
            ):
                matched_books.append(book)

        return matched_books or all_books

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
