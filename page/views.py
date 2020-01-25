from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from .models import User, Comment, Item

# Create your views here.


def index(request):
    users = User.objects.all()
    return render(request, 'page/index.html', )


def mail(request):
    return render(request, 'page/mail.html')


def parcel(request):
    return render(request, 'page/parcel.html')


def logistics(request):
    return render(request, 'page/logistics.html')


def about(request):
    return render(request, 'page/about.html')


def login(request):
    item = Item.objects.all()
    try:
        select = item.get(tracking_number=request.POST['username'])
        item.get(serial_pin=request.POST['password'])
    except(Exception):
        return render(request, 'page/index.html', {'error_message': "number & pin doesnt match"})
    else:
        # session_id = request.COOKIES['sessionid']
        # request.session['logged_in'] = session_id
        request.session['item_id'] = select.id
        return HttpResponseRedirect(reverse('dashboard:dashboard-index'))


def contact(request):
    return render(request, 'page/contact.html')


def profile(request):
    return render(request, 'page/profile.html', {'id': id})


def comment(request):
    try:
        comment = Comment(enquiry=request.POST['comments'], firstname=request.POST['first_name'], lastname=request.POST['last_name'], emailaddress=request.POST['email'],
                           telephone=request.POST['telephone'])
        comment.save()
    except Exception:
        return render(request, 'page/contact.html', {'error_message': "Error Occured, comment not saved"})
    else:
        return render(request, 'page/contact.html', {'success_message': 'Comment saved successfully'})