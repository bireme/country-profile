from django.contrib import admin
from django.urls import path, include

from main import views as main_views


admin.site.site_header = 'Pharmaceutical and Health Technology Country Profile'

urlpatterns = [

    path('', main_views.index, name='index'),
    path('country/<str:country_code>/', main_views.country_page, name='country'),
    path('profile/<str:country_code>/', main_views.profile_page, name='profile'),
    path('update/<int:pk>/', main_views.CountryIndicatorUpdateView.as_view(), name='update'),
    path('create/<str:profile_id>/<str:indicator_id>/', main_views.CountryIndicatorCreateView.as_view(), name='create'),

    path('admin/', admin.site.urls),

    path('tinymce/', include('tinymce.urls')),

]
