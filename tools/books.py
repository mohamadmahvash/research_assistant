from core.models import BaseResearchTool
from .clients import BooksClient


class BooksTool(BaseResearchTool):
    name = "books"

    def __init__(self):
        self.client = BooksClient()

    def can_handle(self, query):
        keywords = [
            "book",
            "books",
            "کتاب",
            "کتاب ها",
        ]

        query = query.lower()
        return any(keyword in query for keyword in keywords)

    def execute(self, query):
        return self.client.search_books(query)
