import requests
import json

from django.conf import settings

# import checksum generation utility
# You can get this utility from https://developer.paytm.com/docs/checksum/
from . import Checksum

# Verify transaction status from paytm api for tampering
def verify_transaction(ORDER_ID):
    # initialize a dictionary
    paytmParams = {}

    # Find your MID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
    MERCHANT_ID = settings.PAYTM_MERCHANT_ID
    paytmParams["MID"] = MERCHANT_ID

    # Enter your order id which needs to be check status for
    paytmParams["ORDERID"] = ORDER_ID

    # Generate checksum by parameters we have
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
    MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
    checksum = Checksum.generate_checksum(paytmParams, MERCHANT_KEY)

    # put generated checksum value here
    paytmParams["CHECKSUMHASH"] = checksum

    # prepare JSON string for request
    post_data = json.dumps(paytmParams)

    if settings.DEBUG:
        # for Staging
        url = "https://securegw-stage.paytm.in/order/status"
    else:
        # for Production
        url = "https://securegw.paytm.in/order/status"
    
    response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
    return response