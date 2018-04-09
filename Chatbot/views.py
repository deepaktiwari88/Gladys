from django.shortcuts import render
from .models import Restaurant

from django.shortcuts import render

def chat(request):
    name = request.session.get('Name')
    context = {'name':name}
    return render(request, 'Chatbot/chat.html', context)

def servequery(request):
    query = request.POST.get('send-request', None)
    context = {}

    if query=='restaurant' and request.method == 'POST':
        results = Restaurant.objects.all()
        context.update({'results':results})

    return render(request, 'Chatbot/chat.html', context)

