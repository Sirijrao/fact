from django.urls import path
from app52.views import home
urlpatterns = [path('', home,name='home'),]