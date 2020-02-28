from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages

from . import Checksum
from . Transaction_status import verify_transaction

from .models import PaymentHistory, OrderHistory


# Create your views here.


@login_required
def home(request):
    return HttpResponse("<html><p>Welcome " + request.user.username + "</p><a href='" + settings.HOST_URL + "/payment'>PayNow</html>")


@login_required
def payment(request, amount):
    user = request.user
    settings.USER = user
    MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
    MERCHANT_ID = settings.PAYTM_MERCHANT_ID
    # REPLACE USERNAME WITH PRIMARY KEY OF YOUR USER MODEL
    CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL + request.user.username + '/'
    # Generating unique temporary ids
    order_id = Checksum.__id_generator__()

    try:
        bill_amount = float(amount)
    except:
        return HttpResponse('<h1>Invalid Amount</h1>')
    if bill_amount:
        data_dict = {
            'MID': MERCHANT_ID,
            'ORDER_ID': order_id,
            'TXN_AMOUNT': bill_amount,
            'CUST_ID': user.username,
            'INDUSTRY_TYPE_ID': settings.INDUSTRY_TYPE_ID,
            'WEBSITE': settings.PAYTM_WEBSITE,
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': CALLBACK_URL,
        }
        param_dict = data_dict
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)

        # Save order to Order History to verify in case of no response is received from paytm
        OrderHistory.objects.create(user= request.user, ORDERID= order_id, TXNAMOUNT = bill_amount)
        return render(request, "paytm_gateway/payment.html", {'paytmdict': param_dict, 'user': user})
    return HttpResponse("Bill Amount Could not find. ?bill_amount=0")

# @login_required
@csrf_exempt
def response(request, user_username):
    if request.method == "POST":
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        if data_dict.get('CHECKSUMHASH', False):
            verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        else:
            verify = False
        if verify:
            for key in request.POST:
                #TXNID changed to CharField
                # if key == "BANKTXNID" or key == "RESPCODE":
                if key == "RESPCODE":
                    if request.POST[key]:
                        data_dict[key] = int(request.POST[key])
                    else:
                        data_dict[key] = 0
                elif key == "TXNAMOUNT":
                    data_dict[key] = float(request.POST[key])
            
            # REPLACE USERNAME WITH PRIMARY KEY OF YOUR USER MODEL
            response = verify_transaction(request.POST['ORDERID'])
            if response.get('RESPCODE') == '01' :
                PaymentHistory.objects.create(user=User.objects.get(username=user_username), **data_dict)
                return render(request, "paytm_gateway/transaction_status.html", {"paytm": data_dict})
            else:
                return HttpResponse("Error Code 144: Transaction verification failed")
        else:
            return HttpResponse("Error Code 143: Checksum verification failed")
    else:
        return HttpResponse("Method \"GET\" not allowed")

    return HttpResponse(status=200)