from django.db import models
from abc import ABC, abstractmethod
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseResearchTool(ABC):

    @abstractmethod
    def can_handle(self, query):
        """
        Check whether this tool can handle the query
        """
        pass

    @abstractmethod
    def execute(self, query):
        """
        Execute external service call
        """
        pass
