from django.shortcuts import render
from .models import Restaurant, Address
from django.template import RequestContext

from django.shortcuts import render,render_to_response

def chat(request):

    query = request.POST.get('message')
    if query=='Restaurant':
        results = Restaurant.objects.all()
        name = request.session.get('Name')

        return render(request,'Chatbot/chat.html', {'results': results, 'query':query, 'name':name})
    else:
        name = request.session.get('Name')
        context = {'name':name}
        return render(request, 'Chatbot/chat.html', context)



