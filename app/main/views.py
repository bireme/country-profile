from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from main.models import *
from main.forms import *

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
    country_profile = Profile.objects.get(country=country)
    country_indicators = CountryIndicatorData.objects.filter(country_indicator__profile=country_profile)

    # aux dict for template for get data from a specific indicator
    country_indicators_data = {}
    for indicator in country_indicators:
        indicator_code = indicator.country_indicator.indicator.code
        if not indicator_code in country_indicators_data:
            country_indicators_data[indicator_code] = []

        country_indicators_data[indicator_code].append(indicator)

    # aux dict for template for check if indicator has data
    country_indicators_ids = { indicator.country_indicator.indicator.code: indicator.country_indicator.id for indicator in country_indicators }

    # sort spliting the code in parts and using the unicode value for the first part. ex. C1.5.1 -> C1 5 1
    indicator_list_sorted = sorted(indicator_list, key=lambda x: [int(part) if part.isdigit() else ord(part[0:1]) for part in x.code.split('.')])


    response_data = {'country': country,
                    'domain_list': domain_list,
                    'indicator_list' : indicator_list_sorted,
                    'profile_list' : profile_list,
                    'country_profile': country_profile,
                    'country_indicators_data': country_indicators_data,
                    'country_indicators_ids': country_indicators_ids,
                    }

    return render(request, 'main/profile.html', response_data)


def update_indicator(request, profile_id, indicator_id):
    if request.method=='POST':
        form = IndicatorForm(request.POST)
        if form.is_valid():
            form.save()

        indicator_form = IndicatorForm()

    return render(request,'main/country_indicator.html', {"indicator_form": indicator_form})

    response_data = {'country_data' : country_data}

    return render(request, 'main/index.html', response_data)


@method_decorator(login_required, name='dispatch')
class CountryIndicatorUpdate(UpdateView):
    """
    Handle creation and update of educational resource
    """

    model = CountryIndicator
    form_class = IndicatorForm

    def get_context_data(self, **kwargs):
        context = super(CountryIndicatorUpdate, self).get_context_data(**kwargs)

        if self.request.POST:
            context['data_formset'] = DataFormSet(self.request.POST, instance=self.object)
        else:
            context['data_formset'] = DataFormSet(instance=self.object)

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        data_formset = context['data_formset']

        if data_formset.is_valid():
            self.object = form.save()

            data_formset.instance = self.object
            data_formset.save()

        return self.render_to_response(self.get_context_data(form=form))
