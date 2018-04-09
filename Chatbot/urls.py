from django.conf.urls import url
from . import views

app_name = "Chatbot"

urlpatterns = [

    url(r'^$', views.chat, name='chat'),
    url(r'^restaurant/$', views.restaurant, name='restaurant'),
    url(r'^user/$', views.user, name='user'),
]