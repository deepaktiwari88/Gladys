from django.shortcuts import render,redirect
from Chatbot.models import Chat
from .models import User

def index(request):
    username = request.POST.get('UserName', None)

    if username and request.method == 'POST':
        user = User(name=username)
        user.save()
        Chat.objects.all().delete()
        msg = "Hello " + username + ". What would you like to see today ?"
        c = Chat(username='Gladys', message=msg, isuser=False)

        c.save()

        return redirect('chatbot:Chatbot')

    else:
        return render(request, 'about/about us.html')
