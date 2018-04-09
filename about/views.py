from django.shortcuts import render,redirect

def index(request):
    name = request.POST.get('UserName', None)
    context={}

    if name and request.method == 'POST':
        request.session['Name'] = name
        return redirect('chatbot:Chatbot')

    else:
        return render(request, 'about/about us.html')
