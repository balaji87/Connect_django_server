from django.http import HttpResponse

import random

def hello_world(request):
    return HttpResponse("Hello World")

def root_page(request):
    return HttpResponse("Root Home Page")

def random_number(request, max_rand=100):
    random_number = random.randrange(0,int(max_rand))

    msg = "Random Number between 0 and %s : %s" %(max_rand,random_number)

    return HttpResponse(msg)