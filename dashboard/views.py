from django.shortcuts import render
from page.models import User
from page.models import Item

# Create your views here.


def index(request):
    try:
        if request.session['item_id'] is not None:
            item = Item.objects.get(id=request.session['item_id'])
            transits = item.transit.all()
            last_transit = item.transit.last()
            context = {
                'item': item,
                'transits': transits,
                'last': last_transit
            }
            return render(request, 'dashboard/index.html', context)
        else:
            return render(request, 'home/index.html')
    except KeyError:
        return render(request, 'home/index.html')


def logout(request):
    try:
        del request.session['item_id']
    except KeyError:
        pass
    return render(request, 'home/index.html')


def profile(request):
    try:
        if request.session['item_id'] is not None:
            item = Item.objects.get(id=request.session['item_id'])
            transits = item.transit.all()
            person = item.owner

            context = {
                'item': item,
                'person': person
            }
            return render(request, 'dashboard/profile.html', context)
        else:
            return render(request, 'home/index.html')
    except KeyError:
        return render(request, 'home/index.html')


def info(request):
    try:
        user = User(firstname=request.POST['input-first-name'],
                    lastname=request.POST['input-last-name'],
                    email=request.POST['input-email'],
                    phone=request.POST['input-phone'],
                    username=request.POST['input-username'],
                    address=request.POST['input-address'],
                    city=request.POST['input-city'],
                    country=request.POST['input-country'],
                    postal=request.POST['input-postal-code'],
                    about=request.POST['input-about'])
        user.save()
    except Exception:
        return render(request, 'dashboard/profile.html', {'error_message': "Error occured, profile not updated"})
    else:
        return render(request, 'dashboard/profile.html', {
            'success': "You have successfully updated your profile"
    })