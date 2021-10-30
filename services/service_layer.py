import requests
import logging
from decouple import config
from constant import BOOKS_URL_BASE, HTTP_CODES, HTTP_ERROR_MESSAGE

logger = logging.getLogger(__name__)

SECRET_KEY = config('API_KEY')
def get_books_from_third_party(keyword):
    try:
        response = requests.get(f'{BOOKS_URL_BASE}?q={keyword}&key={SECRET_KEY}&maxResults=1')

        if response.status_code == HTTP_CODES.SERVICE_UNAVAILABLE.value:
            response_res = {"status_code" : response.status_code, "msg" :  HTTP_ERROR_MESSAGE[HTTP_CODES.SERVICE_UNAVAILABLE.value]}
        elif response.status_code == HTTP_CODES.FORBIDDEN_CLIENT.value:
            response_res = {"status_code" : response.status_code, "msg" :  HTTP_ERROR_MESSAGE[HTTP_CODES.FORBIDDEN_CLIENT.value]}
        elif response.status_code == HTTP_CODES.BAD_REQUEST.value:
            response_res = {"status_code" : response.status_code, "msg" :  HTTP_ERROR_MESSAGE[HTTP_CODES.BAD_REQUEST.value]}
        else:
            print(response.json()['totalItems'])
            if response.json()['totalItems'] > 0:
                bookId = response.json()['items'][0]["id"]
                bookTitle = response.json()['items'][0]['volumeInfo']["title"]
                if "description" in response.json()['items'][0]['volumeInfo']:
                    bookDescription = response.json()['items'][0]['volumeInfo']["description"]
                else:
                    bookDescription = ""
                response_res = {
                    "status_code" : response.status_code,
                    "book" : {
                    "bookId" : bookId,
                    "title" : bookTitle,
                    "description" : bookDescription
                    },
                    "msg" : HTTP_ERROR_MESSAGE[HTTP_CODES.OK.value]
                }
            else:
                response_res = {
                    "status_code" : HTTP_CODES.NO_CONTENT.value,
                    "book" : {},
                    "msg" : HTTP_ERROR_MESSAGE[HTTP_CODES.NO_CONTENT.value]
                }
        print(f"Got response from third party API --->  {response_res['status_code']}")
        logger.info(f"Got response from third party API --->  {response_res['status_code']}")
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e.response)
        response_res = {"status_code" : HTTP_CODES.GENERIC_RESPONSE_ERROR.value, "msg" : HTTP_ERROR_MESSAGE[HTTP_CODES.GENERIC_RESPONSE_ERROR.value]}
        return response_res
        
    return response_res
    
