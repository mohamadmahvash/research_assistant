from .models import InquiriesRequest, InquiryStep
from tools.selector import ToolSelector


def create_step(inquiry, step_name, status, tool="", payload=None, error=""):
    return InquiryStep.objects.create(
        inquiry=inquiry,
        step_name=step_name,
        tool=tool,
        status=status,
        payload=payload,
        error=error,
    )


class InquiryService:

    @staticmethod
    def process(inquiry_request: InquiriesRequest):
        inquiry_request.status = InquiriesRequest.Status.PROCESSING
        inquiry_request.save(update_fields=["status"])
        tool = ToolSelector.select(inquiry_request.query)

        #SELECTION STATUS
        if not tool:
            create_step(
                inquiry_request,
                step_name="Tool Selection",
                status=InquiryStep.Status.FAILED,
                error="No suitable tool found"
            )

            inquiry_request.status = InquiriesRequest.Status.FAILED
            inquiry_request.save(update_fields=["status"])
            return

        create_step(
            inquiry_request,
            step_name="Tool Selection",
            status=InquiryStep.Status.SUCCESS,
            tool=tool.name
        )
        inquiry_request.selected_tool = tool.name
        inquiry_request.save(update_fields=["selected_tool"])

        try:
            result = tool.execute(inquiry_request.query)

        except Exception as e:

            create_step(
                inquiry_request,
                step_name="Tool Execution",
                status=InquiryStep.Status.FAILED,
                tool=tool.name,
                error=str(e)
            )
            inquiry_request.status = InquiriesRequest.Status.FAILED
            inquiry_request.save(update_fields=["status"])
            return

        create_step(
            inquiry_request,
            step_name="Tool Execution",
            status=InquiryStep.Status.SUCCESS,
            tool=tool.name,
            payload=result
        )

        inquiry_request.result = result
        inquiry_request.status = InquiriesRequest.Status.COMPLETED
        inquiry_request.save(update_fields=["result", "status"])

        create_step(
            inquiry_request,
            step_name="Save Result",
            status=InquiryStep.Status.SUCCESS,
            payload=result
        )
