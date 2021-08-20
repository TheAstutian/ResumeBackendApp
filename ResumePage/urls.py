from django.urls import path

from .views import ResumePage, Responses

urlpatterns = [
    path('', ResumePage.as_view(), name='index'),
    path('responses/', Responses.as_view(), name='responses'), 
]