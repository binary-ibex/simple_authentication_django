from django.urls import path 
from .views import *

urlpatterns = [
	path('', home_page, name="home_page"),
	path('login', login_page, name="login_page"),
	path('logout', logout_page, name="logout_page")
]