from django.db import models

# Create your models here.
class Scanned(models.Model):
    num = models.IntegerField()

    def Add(self):
        self.num = self.num +1
        return self.num

    def Subtract(self):
        self.num = self.num -1
        return self.num
