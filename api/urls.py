from django.conf.urls import include, url
from rest_framework import routers
from api import views

#define route
route = routers.DefaultRouter()

#register new address
route.register(r'student', views.StudentViewSet)
#route.register(r'add_student', views.AddStudentViewSet)

#register upper route and add
urlpatterns = [
    url('api/', include(route.urls)),
    url(r'_ping', views._ping),
    url(r'query_ip',views.query_ip),
]
