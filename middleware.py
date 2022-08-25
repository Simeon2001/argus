from .eyes import watch

# Argus middleware

class ArgusEyesMiddleware:
    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        watch(request, response)

        return response
