from rest_framework.response import Response


def response(status, message, data):
    payload = {
        'status':status,
        'message':message,
        'data':data
    }

    return Response(payload)