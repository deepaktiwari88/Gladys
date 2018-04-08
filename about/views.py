from django.shortcuts import render

def index(request):
    name = request.POST.get('UserName', None)
    if name and request.method == 'POST':
        context = {'name':name}
        return render(request, 'Chatbot/chat.html', context)

    else:
        return render(request, 'about/about us.html')
