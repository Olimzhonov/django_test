from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    return render (request, './index.html')
    

def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name = name, order_phone = phone)
        element.save()
        sendTelegram(tg_name = name, tg_phone = phone)
        return render(request, './thanks.html', { 'name': name,})
    else:
        return render(request, './thanks.html')