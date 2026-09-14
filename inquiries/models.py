from django.db import models
from core.models import BaseModel
from django.conf import settings


class InquiriesRequest(BaseModel):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PROCESSING = "processing", "Processing"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="research_requests")
    query = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    selected_tool = models.CharField(max_length=50, blank=True)
    result = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.user} - {self.status}"


class InquiryStep(models.Model):
    class Status(models.TextChoices):
        SUCCESS = "success", "Success"
        FAILED = "failed", "Failed"

    inquiry = models.ForeignKey(InquiriesRequest, on_delete=models.CASCADE, related_name="steps")

    step_name = models.CharField(max_length=100)
    tool = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices)
    payload = models.JSONField(null=True, blank=True)
    error = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
