# GEWA Wallet
GEWA Wallet is a wallet service made for use within the Organiztions for convinient tranfer and mangement of finances. The generated data can further be processed as required.
GEWA Wallet uses Django Framework, MySQL as the database and Paytm as the payment gateway.

# Setting the Project
## Linux Installation
1. Clone the project
```sh
$ git clone https://github.com/monuyadav016/gewa_wallet.git
```

2. Create python virtual environment inside the cloned repository and activate it and install the requirements
```sh
$ python -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

3. Modify MySQL User and Database details in the settings.py file
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'DATABASE_NAME',
        'USER': 'DATABASE_USER', 
        'PASSWORD': 'DATABASE_USER_PASSWORD',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

4. Modify Paytm Merchant details such as YOUR_MERCHANT_ID, YOUR_MERCHANT_KEY, PAYTM_WEBSITE details in the setting.py file (Make sure to keep the staging and deployment details seperate)
```sh
INDUSTRY_TYPE_ID = 'Retail'
PAYTM_CALLBACK_URL = "/gateway/paytm/response/"

if DEBUG:
    PAYTM_MERCHANT_KEY = "YOUR_MERCHANT_KEY"
    PAYTM_MERCHANT_ID = "YOUR_MERCHANT_ID"
    PAYTM_WEBSITE = 'WEBSTAGING'
    HOST_URL = 'http://localhost:8000'
```

5. Make and Run Migrations
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

### Development

Want to contribute? Great!


## License
