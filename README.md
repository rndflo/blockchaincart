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

//------------------------------------------------------------------------------------------------------------------------------------
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

//------------------------------------------------------------------------------------------------------------------------------------
Add to INSTALLED_APPS in settings.py

    'rest_framework',
    'shop',


//------------------------------------------------------------------------------------------------------------------------------------

Add Product model to models.py

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=False)


    def __str__(self):
        return self.title
    
 
//------------------------------------------------------------------------------------------------------------------------------------   

