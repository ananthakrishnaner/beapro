
# BEAPRO

It is a job platform for tutors and learning platform for students, Help to connect student and tutor.
![Logo](https://raw.githubusercontent.com/ananthakrishnaner/beapro/main/example/img/beaprologo.png?token=GHSAT0AAAAAABUDAWYOZTSM7EO6G7UJTMQYYTNHYQA)


## Installation



```bash
  git clone https://github.com/ananthakrishnaner/beapro.git
  cd beapro
```

create a file secretfile.py

  ```python
SECRET_KEY='Add your django secret key here'
DEBUG=True


#Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT =587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your email id'
EMAIL_HOST_PASSWORD = 'your password'

#payment
RAZOR_KEY_ID = 'razorpay key id'
RAZOR_KEY_SECRET = 'razorpay secret key'

#Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db name here',
        'USER': 'db user here',
        'PASSWORD':'db password here',
        'HOST':'localhost'
    }
}

#sms
account_sid ='twilio account sid'
auth_token ='twilio auth token'
sms_number = 'twilio phone number'
```  

create a virtual enviornment & activate it 
> ` I used :- virtualenv  `

```sh
pip install requirements.py
python manage.py makemigrations
python manage.py migrate
```

To create admin account 

```sh
python manage.py createsuperuser
```

To run application

```sh
python manage.py runserver
```


## Some Screenshots

![App Screenshot](https://raw.githubusercontent.com/ananthakrishnaner/beapro/main/example/img/screenshot1.JPG?token=GHSAT0AAAAAABUDAWYP6OY3O3PQIX3YOWUKYTNIZMQ)

![App Screenshot](https://raw.githubusercontent.com/ananthakrishnaner/beapro/main/example/img/screenshot2.JPG?token=GHSAT0AAAAAABUDAWYOSTX4K2FTF4XBHRHUYTNI2BQ)

![App Screenshot](https://raw.githubusercontent.com/ananthakrishnaner/beapro/main/example/img/screenshot3.JPG?token=GHSAT0AAAAAABUDAWYPPISNOJ7TJKMMTN4OYTNI2RQ)

![App Screenshot](https://raw.githubusercontent.com/ananthakrishnaner/beapro/main/example/img/screenshot4.JPG?token=GHSAT0AAAAAABUDAWYO2UWEQWJ2PVG7H7H6YTNI3KQ)

![App Screenshot](https://raw.githubusercontent.com/ananthakrishnaner/beapro/main/example/img/screenshot5.JPG?token=GHSAT0AAAAAABUDAWYOC3FMV2JVPTPZNBDMYTNI32Q)

![App Screenshot](https://raw.githubusercontent.com/ananthakrishnaner/beapro/main/example/img/screenshot6.JPG?token=GHSAT0AAAAAABUDAWYP627G6FOTOOM35MVAYTNI4JQ)


## 🚀 About Me
contact:- ananthakrishnan1464@gmail.com

