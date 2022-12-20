from django.urls import path
from .api.views import CreateNote, ListNote, UpdateNote, DeleteNote
# from django.urls import re_path as url, include

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('new/', CreateNote.as_view(), name='create'),
    path('', ListNote.as_view(), name='list'),
    path('edit/<int:pk>', UpdateNote.as_view(), name='edit'),
    path('delete/<int:pk>', DeleteNote.as_view(), name='delete'),
]
app_name = 'notes'
