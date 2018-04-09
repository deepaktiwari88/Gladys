from django.conf.urls import url
from . import views

app_name = "chatbot"

urlpatterns = [

    url(r'^bot/$', views.chat, name="Chatbot"),
]