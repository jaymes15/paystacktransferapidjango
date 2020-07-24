from . import views
from django.conf.urls import url
from django.urls import path



app_name= 'paystacktransapp'
urlpatterns = [
	path('',views.homepage, name='homepage'), 
	
	]