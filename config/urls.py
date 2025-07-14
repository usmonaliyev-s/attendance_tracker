from django.contrib import admin
from django.urls import path, include

from attendance_tracker.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('index/', index, name='index'),
    path('history/', history, name='history'),
    path('courses/', include('courses.urls')),
    path('teachers/', include('teachers.urls')),
    path('students/', include('students.urls')),
    path('marking-attendace/', include('attendance_tracker.urls')),
    path('accounts/', include('accounts.urls')),
]
