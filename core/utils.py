from rest_framework import status as http_status
from rest_framework.response import Response


def get_api_error_response(message, status=None, data=None):
    """
    returns an error message if there is an error in API
    :param message: error message from request
    :type message: str
    :param status: status of the request
    :param data: data to be sent in response on failure
    :return: returns the Response object
    """
    status = status or http_status.HTTP_400_BAD_REQUEST

    if isinstance(message, str) and data is not None and isinstance(data, list) or isinstance(data, dict):
        return Response({"message": message, "data": data}, status=status)

    if isinstance(message, str):
        return Response({"message": message}, status=status)
    return Response(message, status=status)


def get_api_success_response(message=None, data=None, status=None):
    """
    returns a success response whenever API is hit successfully
    :param message: message to indicate the status of response
    :type message: str
    :param data: response data
    :type data: list or dict
    :param status: status
    :return: returns the Response object
    """
    status = status or http_status.HTTP_200_OK

    if data is not None and isinstance(data, list) or isinstance(data, dict):
        return Response(data, status=status)
    if message:
        return Response({"message": message}, status=status)
    return Response(status=status)
