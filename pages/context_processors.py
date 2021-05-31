from messagefromceo.models import Message
from visafacts.models import VisaDetail
from servicePage.models import Service

def message_context_processor(request):

    message = Message.objects.all()
    visas = VisaDetail.objects.all()
    service = Service.objects.all()
    context = {
        "message": message,
        "visas": visas,
        "service": service
    }

    return context
