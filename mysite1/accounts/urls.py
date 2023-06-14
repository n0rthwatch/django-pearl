from django.urls import path

from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('authentication/', authentication, name='authentication'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]

