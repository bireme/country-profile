from django.shortcuts import render
from django.db.models.functions import Substr

from main.models import *

def index(request):
    profile_list = Profile.objects.all().order_by('country__name')
    response_data = {'profile_list' : profile_list}

    return render(request, 'main/index.html', response_data)


def country_page(request, country_code):
    country_data = Profile.objects.get(country__code=country_code)
    response_data = {'country_data' : country_data}

    return render(request, 'main/country.html', response_data)


def profile_page(request, country_code):
    profile_list = Profile.objects.all().order_by('country__name')
    domain_list = Domain.objects.all().order_by('number')
    indicator_list = Indicator.objects.all()
    country = Country.objects.get(code=country_code)

    # sort spliting the code in parts and using the unicode value for the first part. ex. C1.5.1 -> C1 5 1
    indicator_list_sorted = sorted(indicator_list, key=lambda x: [int(part) if part.isdigit() else ord(part[0:1]) for part in x.code.split('.')])

    response_data = {'country': country,
                    'domain_list': domain_list,
                    'indicator_list' : indicator_list_sorted,
                    'profile_list' : profile_list}

    return render(request, 'main/profile.html', response_data)
