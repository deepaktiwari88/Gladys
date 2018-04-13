from django.http import JsonResponse
from .models import Restaurant, Chat
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from about.models import User

def Post(request):
    if request.method == 'POST':
        msg = request.POST.get('message', None)
        username = User.objects.all().order_by('-id')[0].name
        c = Chat(username=username, message=msg, isuser=True)

        if msg != '':
            c.save()

        if msg=='Restaurant':
            for restaurant in Restaurant.objects.all():
                name = restaurant.name
                shop_no = restaurant.address.shop_no
                sector = restaurant.address.sector
                city = restaurant.address.city
                rating = restaurant.rating

                response = mark_safe("Name : " + name + "<br>Rating : " + str(rating) +  "<br>Address : " + str(shop_no) + "<br>Sector: " + str(sector) + " ," + city)

                c = Chat(username='Gladys', message=response, isuser=False)

                c.save()

        return JsonResponse({'msg': msg, 'username':username})
    else:
        HttpResponse('Request must be POST')

def chat(request):
    c = Chat.objects.all()
    return render(request, 'Chatbot/chat.html', {'chat': c})

def Messages(request):
    c = Chat.objects.all()
    return render(request, 'Chatbot/messages.html', {'chat': c})

