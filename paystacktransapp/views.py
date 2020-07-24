from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import requests
import json
from django.http import HttpResponse

# Create your views here.


def homepage(request):
	headers = {
    				'Authorization: Bearer sk_test_1590017dabc1772e81fd0e246379f6e6ebcfac80',
                  }
	response = requests.get('https://api.paystack.co/bank', headers={
    				'Authorization': 'Bearer sk_test_1590017dabc1772e81fd0e246379f6e6ebcfac80',
                  })
	if response.status_code == 200:
		result = response.json()
		context = {'result':result}
	return render(request,'paystacktransapp/homepage.html',context)