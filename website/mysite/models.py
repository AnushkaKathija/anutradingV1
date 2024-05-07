from django.db import models

# Create your models here.
class Contact(models.Model):
    companyName = models.CharField(max_length = 122)
    personName = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    phoneNumber = models.CharField(max_length = 122)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.personName