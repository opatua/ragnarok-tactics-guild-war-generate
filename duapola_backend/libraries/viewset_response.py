from rest_framework.renderers import JSONRenderer
from http import HTTPStatus


class ViewsetJSONRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status = renderer_context.get('response').status_code
        response = {
            'status': status,
            'response': data if status == HTTPStatus.OK else [],
            'error': data if status != HTTPStatus.OK else [],
        }
        renderer_context.get('response').status_code = HTTPStatus.OK

        return super().render(response, accepted_media_type=accepted_media_type, renderer_context=renderer_context)
