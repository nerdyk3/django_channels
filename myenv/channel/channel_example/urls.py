from django.urls import path
from channel_example.views import user_list
urlpatterns = [
    path('', user_list,name='user_list'),
]
