def ajax_required(ret_unexcepted):
    def _ajax_required(func):
        def wrapper(request, *args, **kwargs):
            if not request.is_ajax():
                return ret_unexcepted
            return func(request, *args, **kwargs)
        return wrapper
    return _ajax_required