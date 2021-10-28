from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializer import TaskSerializer
from . models import Task

# Create your views here.
@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update':'/task-update/<str:pk/',
        'Delete':'/task-delete/<str:pk/'
    }

    return Response(api_urls)

@api_view(['GET'])
def get_all_task(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_task_by_id(request, id):
    task = Task.objects.get(id= id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def update_task_by_id(request, id):
    task = Task.objects.get(id = id)
    serializer = TaskSerializer(instance = task ,data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_task(request,id):
    task = Task.objects.get(id = id)
    task.delete()
    return Response("Item deleted successfully")
