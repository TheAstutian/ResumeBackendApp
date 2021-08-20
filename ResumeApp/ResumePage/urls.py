from django.urls import path

from .views import ResumePage

urlpatterns = [
    path('', ResumePage.as_view(), name='index'), 
]