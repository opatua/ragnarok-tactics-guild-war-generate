from rest_framework.views import exception_handler
from rest_framework import status

from duapola_backend.utils.api_response import response

def custom_exception_handler(exc, context):
    exception_response = exception_handler(exc, context)

    error_data = []

    if exception_response is not None:
        
        for key, value in exception_response.data.items():
            error = {'field': key, 'message': value}
            error_data.append(error)

        return response(status.HTTP_400_BAD_REQUEST, 'Bad Request', error_data)

    return exception_response
