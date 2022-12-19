from django.urls import include, path
from . import views
# from django.urls import re_path as url, include

urlpatterns = [
    # path('notes/', include('notes.urls')),
    path('', views.home, name='home'),
]
app_name = 'notes'
