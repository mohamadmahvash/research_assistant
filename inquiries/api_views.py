from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from .models import InquiriesRequest
from .serializers import InquiriesRequestSerializer, InquiryRequestDetailSerializer
from .services import InquiryService
from .selectors import get_inquiry_by_user, get_inquiry_by_id_user
from core.pagination import InquiryPagination
from core.permissions import IsOwner


class InquiriesRequestCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = InquiriesRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        research = serializer.save(user=request.user)
        InquiryService.process(research)

        serializer_data = InquiriesRequestSerializer(research)
        return Response(serializer_data.data, status=status.HTTP_201_CREATED)


class InquiriesRequestListAPIView(APIView):
    permission_classes = [IsOwner]

    def get(self, request):
        researches = get_inquiry_by_user(user=request.user)
        self.check_object_permissions(request, researches)

        paginator = InquiryPagination()
        paginated_queryset = paginator.paginate_queryset(researches, request)
        serializer_data = InquiriesRequestSerializer(paginated_queryset, many=True)

        return paginator.get_paginated_response(serializer_data.data)


class InquiriesRequestDetailAPIView(APIView):
    permission_classes = [IsOwner]

    def get(self, request, pk):
        try:
            research = get_inquiry_by_id_user(u_id=pk, user=request.user)
            self.check_object_permissions(request, research)
        except InquiriesRequest.DoesNotExist:
            raise NotFound("Research request not found")

        serializer_data = InquiryRequestDetailSerializer(research)
        return Response(serializer_data.data)
