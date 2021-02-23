from django.shortcuts import render
from .models import Member


def members(request):
    members = Member.objects.all().order_by('Name')
    return render(request, 'members.html', {
        'members': members
    })


def about_us(request):
    return render(request, 'about-us.html')
