from rest_framework.renderers import JSONRenderer
from http import HTTPStatus


class ViewsetJSONRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        success_code = [
            HTTPStatus.OK,
            HTTPStatus.CREATED,
            HTTPStatus.NO_CONTENT
        ]
        status = renderer_context.get('response').status_code
        response = {
            'status': status,
            'response': data if status in success_code else [],
            'error': data if status not in success_code else [],
        }
        renderer_context.get('response').status_code = HTTPStatus.OK

        return super().render(response, accepted_media_type=accepted_media_type, renderer_context=renderer_context)
