from django.shortcuts import render
from .models import Restaurant, User

from django.shortcuts import render     # for linking with templates ie HTML file

def chat(request):
    return render(request, 'Chatbot/chat.html', {})

def restaurant(request):        # for displaying all restaurants
    query = request.POST.get('send-request', None)
    # context = {}

    all_restaurants = Restaurant.objects.all()
    # context.update({'results':results})
    context = {
        'all_restaurants': all_restaurants,
    }

    return render(request, 'Chatbot/restaurant.html', context)  # it redirects to another page /restaurant JUST FOR TESTING


def user(request):        # for displaying all users
    query = request.POST.get('send-request', None)
    # context = {}

    all_users = User.objects.all()
    # context.update({'results':results})
    context = {
        'all_users': all_users,
    }

    return render(request, 'Chatbot/user.html', context)  # it redirects to another page /restaurant JUST FOR TESTING

