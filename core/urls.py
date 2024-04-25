from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',peoples,name='peoples'),
    path('employee/',employees,name='employee'),
    path('delete_employee/<employee_id>/',delete_employee, name='delete_employee'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()


