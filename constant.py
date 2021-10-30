from decouple import config
from enum import Enum

BOOKS_URL_BASE = f'https://www.googleapis.com/books/v1/volumes'


class HTTP_CODES(Enum):
    GENERIC_RESPONSE_ERROR = 500
    SERVICE_UNAVAILABLE = 503
    FORBIDDEN_CLIENT = 403
    BAD_REQUEST = 400
    NO_CONTENT = 204
    OK = 200

HTTP_ERROR_MESSAGE = {
    500: "500 generic error response",
    503: "503 Service Unavailable",
    403: "403 Forbidden client",
    400: "400 Bad Request response",
    204: "204 No Content",
    200: "OK"
}
