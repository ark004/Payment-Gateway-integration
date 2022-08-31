from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import razorpay

RAZORPAY_API_KEY = 'rzp_test_2MLZUnuE6gCPwc'
RAZORPAY_API_SECRET_KEY = 'Np1xnnLZBD6S97IUNJSsIaW6'
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

# def home(request):
#
#     return render(request,'index.html')
def index(request):
                amount = 100*100
                currency = 'INR'
                payment_order = client.order.create(dict(amount=amount,currency=currency,payment_capture=1))
                payment_order_id = payment_order['id']
                context={
                    'api_key':RAZORPAY_API_KEY,'order_id':payment_order_id
                }

                return render(request,'home.html',context)
