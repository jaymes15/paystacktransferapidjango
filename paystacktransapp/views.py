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
	try:
		if response.status_code == 200:
			results = response.json()
			result = results['data']
			context = {'result':result}
			return render(request,'paystacktransapp/homepage.html',context)
	except Exception as ex:
		context = {"error":ex}
		return render(request,'paystacktransapp/homepage.html',context)


def checkaccount(request):
	try:
		print("hello")
		bankcode = request.POST.get('bankcode',None)
		accountnumber = request.POST.get('accountnumber',None)
		headers = {
    				'Authorization: Bearer sk_test_1590017dabc1772e81fd0e246379f6e6ebcfac80',
                  }
		response = requests.get('https://api.paystack.co/bank/resolve?account_number='+accountnumber+'&bank_code='+bankcode, headers={
        			      'Authorization': 'Bearer sk_test_1590017dabc1772e81fd0e246379f6e6ebcfac80',
        	           })
		if response.status_code == 200:
			results = response.json()
			return JsonResponse(results)
		else:
			return HttpResponseBadRequest()
				
	except Exception as ex:
		context = {"error":ex}
		return render(request,'paystacktransapp/homepage.html',context)		
    				
