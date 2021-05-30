from messagefromceo.models import Message
from visafacts.models import VisaDetail

def message_context_processor(request):

    message = Message.objects.all()
    visas = VisaDetail.objects.all()
    context = {
        "message": message,
        "visas": visas
    }

    return context
