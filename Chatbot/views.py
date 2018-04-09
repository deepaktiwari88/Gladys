from django.shortcuts import render
from .models import Restaurant

from django.shortcuts import render

def chat(request):
    return render(request, 'Chatbot/chat.html', {})

def servequery(request):
    query = request.POST.get('send-request', None)
    context = {}

    if query=='restaurant' and request.method == 'POST':
        results = Restaurant.objects.all()
        context.update({'results':results})

    return render(request, 'Chatbot/chat.html', context)

