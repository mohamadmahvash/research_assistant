from rest_framework import serializers
from .models import InquiriesRequest, InquiryStep


class InquiriesRequestSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d/%m/%Y - %H:%M")
    updated = serializers.DateTimeField(format="%d/%m/%Y - %H:%M")

    class Meta:
        model = InquiriesRequest

        fields = [
            "id",
            "query",
            "status",
            "selected_tool",
            "result",
            "created",
            "updated",
        ]
        read_only_fields = [
            "status",
            "selected_tool",
            "result",
            "created",
            "updated",
        ]


class InquiryStepSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True, format="%d/%m/%Y - %H:%M")

    class Meta:
        model = InquiryStep

        fields = [
            "step_name",
            "tool",
            "status",
            "payload",
            "error",
            "created",
        ]


class InquiryRequestDetailSerializer(serializers.ModelSerializer):
    steps = InquiryStepSerializer(many=True, read_only=True)
    created = serializers.DateTimeField(read_only=True, format="%d/%m/%Y - %H:%M")
    updated = serializers.DateTimeField(read_only=True, format="%d/%m/%Y - %H:%M")

    class Meta:
        model = InquiriesRequest

        fields = [
            "id",
            "query",
            "status",
            "selected_tool",
            "result",
            "created",
            "updated",
            "steps",
        ]
