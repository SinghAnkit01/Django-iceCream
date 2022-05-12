from django.db import models

# Create your models here.
# models always define database
class Contact(models.Model):
    # contact is a table which stores the value of form fiels like name,email,desc etc
    # makemigrations means create changes and stores in a file
    # migrate apply the pending changes created by makemigrations.
    name = models.CharField(max_length=122)
    # something like name varchar(20)
    # in django charfield,datefield,textfield this all are field use to define data-type and laength in django
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
   
    # run python manage.py makemigrations for detecting changes
    # if no change detected there are two ways to detect changes
    # first register your model in admin.py
    # second register your app in settings.py 
    
    # show name instead of showing contact object(3) and contact object(2).
    def __str__(self):
        return self.name
    
    
    
    
    

