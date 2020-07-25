from . import views
from django.conf.urls import url
from django.urls import path



app_name= 'paystacktransapp'
urlpatterns = [
	path('',views.homepage, name='homepage'), 
	path('checkaccount/',views.checkaccount,name="checkaccount"),
	path('generate_receipt/',views.generate_receipt,name="generate_receipt")
	
	]