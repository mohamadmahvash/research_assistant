from .models import InquiriesRequest


def get_inquiry_by_id_user(*, u_id, user):
    return InquiriesRequest.objects.get(id=u_id, user=user)


def get_inquiry_by_user(*, user):
    return InquiriesRequest.objects.filter(user=user).order_by("-created")
