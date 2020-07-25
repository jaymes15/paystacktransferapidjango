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
		
		global bankcode
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
			global acccount_details 
			acccount_details = results
			return JsonResponse(results)
		else:
			return HttpResponseBadRequest()
				
	except Exception as ex:
		context = {"error":ex}
		return render(request,'paystacktransapp/homepage.html',context)	




def generate_receipt(request):
	try:
		amount = request.POST.get('amount',None)

		he = {"Authorization": "Bearer sk_test_1590017dabc1772e81fd0e246379f6e6ebcfac80","Content-Type" : "application/json"}
		info ={"type": "nuban",
		        "name": str(acccount_details['data']['account_name']),
				"account_number": str(acccount_details['data']['account_number']),
				"bank_code": str(bankcode),
				"currency": "NGN"
				}
		try:
			response = requests.post("https://api.paystack.co/transferrecipient",json=info,headers=he)
			if response.status_code == 201:
					results = response.json()
					global receipt
					receipt = results
					he = {"Authorization": "Bearer sk_test_1590017dabc1772e81fd0e246379f6e6ebcfac80","Content-Type" : "application/json"}
					info ={ "source": "balance",
							 "amount": int(amount),
							 "recipient": str(receipt['data']['recipient_code']),
							 "reason": "Holiday Flexing" 
							 }
							 
					response = requests.post("https://api.paystack.co/transfer",json=info,headers=he)
					if response.status_code == 201:
								message={"message":"You have been credited"}
								return JsonResponse(message)
					else:
							
							message={"message":"You cannot initiate third party payouts as a starter business"}
							return JsonResponse(message)		
		except Exception as ex:
			message={"message":ex}
			return JsonResponse(message)		
					
	except Exception as ex:
		message={"message":ex}
		return JsonResponse(message)

				











    				
