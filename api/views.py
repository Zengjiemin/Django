from .models import Student
from .serializers import StudentSerializers
from django.forms.models import model_to_dict
from rest_framework import viewsets
from django.http import HttpResponse

import socket
import json
import syslog
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('pk')
    serializer_class = StudentSerializers    


def _ping(request):
    return HttpResponse("I am alive GoT!")

def query_ip(request):
    return HttpResponse(socket.gethostbyname(socket.gethostname()))

def add_student(request):
    response = {'status':True,'message': None,'data':None}
    try:
        a = request.POST.get('age')
        # print(a)
        n = request.POST.get('name')
        # print(n)
        obj = Student.objects.create(age=a, name=n)

        response['data'] = obj.name
        
        # write to log
        dic_obj = model_to_dict(obj)
        del dic_obj['id']
        res = json.dumps(dic_obj)
    
        f = open('server.log', 'a+')
        f.write(res+'\n')
        f.close()
        # syslog.openlog('var/log/server.log')
        # syslog.syslog(res)
        # syslog.closelog()

    except Exception as e:
        response['status'] = False
        response['message'] = 'wrong input!'

    # print("GoT!")
    result = json.dumps(response,ensure_ascii=False) 
    return HttpResponse(result)
