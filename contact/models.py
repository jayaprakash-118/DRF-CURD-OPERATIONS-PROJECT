from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)

 #   class Meta:
   #     verbose_name=("contacts")
    #    verbose_name_plural=("contacts")

    def __str__(self):
        return self.name