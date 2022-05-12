from django.contrib import admin
from home.models import Contact
# home is my app and i have a table named as Contact 
# Register your models here.

admin.site.register(Contact)
# registering Contact table on admin site
