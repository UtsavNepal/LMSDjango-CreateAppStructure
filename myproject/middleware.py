import logging

# Initialize logger
logger = logging.getLogger('transaction_logger')

class LogRequestMiddleware:
    """
    Middleware to log requested URLs.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the requested URL
        logger.info(f"Requested URL: {request.path}")

        # Proceed with the request-response cycle
        response = self.get_response(request)

        return response
