import json

from django.http import HttpResponse

__all__ = []


class JsonAsHTML(object):
    """
    View a JSON response in your browser as HTML
    Useful for viewing stats using Django Debug Toolbar

    This middleware should be place AFTER Django Debug Toolbar middleware
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # only do something if this is a json response
        if response["Content-Type"] == "application/json":
            content = response.content
            try:
                json_ = json.loads(content)
                content = json.dumps(json_, sort_keys=True, indent=2)
            except ValueError:
                pass
            response = HttpResponse(
                "<html><body><pre>{}</pre></body></html>".format(content)
            )
            response["Content-Type"] = "text/html;charset=utf-8"
        return response
