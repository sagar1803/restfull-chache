from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import exceptions

from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializer import BookSerializer
from . models import Books

from services.service_layer import get_books_from_third_party

import logging

from constant import HTTP_CODES, HTTP_ERROR_MESSAGE


# Create your views here.
logger = logging.getLogger(__name__)


@api_view(['GET'])
def get_book_by_matching_name(request, keyword):
    try:
        check_book = Books.objects.filter(title__icontains = keyword).exists()
        if check_book:
            book = Books.objects.filter(title__icontains = keyword)
            serializer = BookSerializer(book, many=True)
            print("Data present in db")
            return Response(serializer.data)
        else:
            print("Fetch the data from third part api")
            get_data = get_books_from_third_party(keyword)
            if get_data['status_code'] == HTTP_CODES.OK.value:
                book = Books(bookId = get_data['book']['bookId'], title = get_data['book']['title'], description = get_data['book']['description'])
                book.save()
            return Response(get_data,status = get_data['status_code'])
    except exceptions as e:
        print(str(e))
        logging(e)
        return Response(str(e), HTTP_ERROR_MESSAGE[HTTP_CODES.GENERIC_RESPONSE_ERROR.value])
        


