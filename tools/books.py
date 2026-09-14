from core.models import BaseResearchTool


class BooksTool(BaseResearchTool):
    name = "books"

    def can_handle(self, query):
        keywords = ["book", "books", "کتاب"]
        query = query.lower()
        return any(keyword in query for keyword in keywords)

    def execute(self, query):
        return {
            "tool": self.name,
            "query": query,
            "results": []
        }
