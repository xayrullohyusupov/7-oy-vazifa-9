from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_show = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.full_name



class ChooseItem(models.Model):
    icon = models.ImageField(upload_to='icons/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/')
    youtube = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
from django.db import models

class Partner(models.Model):
    image = models.ImageField(upload_to='partner_images/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.alt_text if self.alt_text else 'Partner Image'

