from vote4film.log import global_context_filter


def add_request_logging_context(get_response):
    """Set additional request-related information for logging.

    This should be the first middleware that is called.
    """

    def middleware(request):
        global_context_filter.start_request(request)
        response = get_response(request)
        global_context_filter.end_request()
        return response

    return middleware


def add_user_logging_context(get_response):
    """Set additional request-related information for logging.

    This should be after the authentication middleware.
    """

    def middleware(request):
        global_context_filter.update_user_info()
        return get_response(request)

    return middleware
