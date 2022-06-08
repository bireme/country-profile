from django.shortcuts import render

from main.models import Profile

def index(request):

    profile_lists = Profile.objects.all()

    response_data = {'profile_lists' : profile_lists}

    return render(request, 'main/index.html', response_data)