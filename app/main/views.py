from django.shortcuts import render
from django.db.models.functions import Substr

from main.models import Profile, Indicator

def index(request):

    profile_lists = Profile.objects.all()
    indicator_list = Indicator.objects.all()

    # sort spliting the code in parts and using the unicode value for the first part. ex. C1.5.1 -> C1 5 1
    indicator_list_sorted = sorted(indicator_list, key=lambda x: [int(part) if part.isdigit() else ord(part[0:1]) for part in x.code.split('.')])

    response_data = {'profile_lists' : profile_lists}

    return render(request, 'main/index.html', response_data)