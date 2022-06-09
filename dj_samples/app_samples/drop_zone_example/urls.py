from django.urls import path

from .views import DropView, upload_file

urlpatterns = [
    path('dp_zone/', DropView.as_view(), name='dp_zone'),
    path('upload/', upload_file, name='upload')
]
