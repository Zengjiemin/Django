from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers

from rest_framework import viewsets
from django.http import HttpResponse
import socket
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('pk')
    serializer_class = StudentSerializers

#class AddStudentViewSet(viewsets.ModelViewSet):
    

def _ping(request):
    return HttpResponse("I am alive GoT!")

def query_ip(request):
    return HttpResponse(socket.gethostbyname(socket.gethostname()))
