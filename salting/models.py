from django.db import models

# Create your models here.
class salting(models.Model):
    username=models.CharField(max_length=64)
    password=models.CharField(max_length=64)
    salt=models.CharField(max_length=64)
    salt_pos=models.CharField(max_length=64)
    

    def __str__(self):
        return f"ID : {self.id} Your username: {self.username} and your password:  {self.password} , salt: {self.salt},         salt position: {self.salt_pos}"

