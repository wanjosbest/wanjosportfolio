from django.db import models

# contact me for services
class service(models.Model):
    name = models.CharField(max_length=100,null=True,unique=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField(max_length=100, null=True, unique=True)
    name = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    service = models.ForeignKey(service, related_name="service_contact",on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.service} By {self.name}"
    
    
    
