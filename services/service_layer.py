import requests
import logging
from decouple import config

logger = logging.getLogger(__name__)

SECRET_KEY = config('API_KEY')
def get_books_from_third_party(keyword):
    try:
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={keyword}&key={SECRET_KEY}&maxResults=1')
        if response.status_code == 503:
            response_res = {"status_code" : response.status_code, "msg" : "503 Service Unavailable"}
        elif response.status_code == 403:
            response_res = {"status_code" : response.status_code, "msg" : "403 Forbidden client"}
        elif response.status_code == 400:
            response_res = {"status_code" : response.status_code, "msg" : "400 Bad Request response"}
        else:
            print(response.json()['totalItems'])
            if response.json()['totalItems'] > 0:
                bookId = response.json()['items'][0]["id"]
                bookTitle = response.json()['items'][0]['volumeInfo']["title"]
                bookDescription = response.json()['items'][0]['volumeInfo']["description"]
                response_res = {
                    "status_code" : response.status_code,
                    "book" : {
                    "bookId" : bookId,
                    "title" : bookTitle,
                    "description" : bookDescription
                }
                }
            else:
                response_res = {
                    "status_code" : 204,
                    "book" : {},
                    "msg" : "204 No Content"
                }
        print(f"Got response from third party API --->  {response_res['status_code']}")
        logger.info(f"Got response from third party API --->  {response_res['status_code']}")
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        logger.error(SystemExit(e))
        raise SystemExit(e)
        
    return response_res
    
