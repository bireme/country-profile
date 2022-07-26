from django.contrib import admin
from django.urls import path, include

from main import views as main_views

urlpatterns = [

    path('', main_views.index, name='index'),
    path('country/<str:country_code>/', main_views.country_page, name='country'),
    path('profile/<str:country_code>/', main_views.profile_page, name='profile'),

    path('admin/', admin.site.urls),

    path('tinymce/', include('tinymce.urls')),

]
