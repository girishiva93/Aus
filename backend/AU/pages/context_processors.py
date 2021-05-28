from messagefromceo.models import Message


def message_context_processor(request):
    """
        Context processor for courses
        Gets all the course object and makes it globally available in templates
    """

    message = Message.objects.all()

    context = {
        "message": message
    }

    return context
