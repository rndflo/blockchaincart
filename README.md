# blockchaincart
Open source implementation of shopping cart integrated with blockchain technology

## Steps

==> django-admin.py startproject blockchaincart


==> python3 -m venv venv

==> source venv/bin/activate

==> pip3 install -r requirements.txt

==> python manage.py startapp shop

==> python manage.py makemigrations

==> python manage.py migrate

Add TEMPLATES directive to settings.py


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]