from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.

class User(models.Model):
    ism=models.CharField(max_length=50,blank=False)
    familiya=models.CharField(max_length=50,blank=False)
    yosh=models.PositiveIntegerField(default=16,blank=True)
    picture=models.ImageField(upload_to='images/',default='images/default.jpg',blank=True)
    slag=models.SlugField(blank=True,unique=True)
    def save(self, *args, **kwargs):
        if not self.slag:
            self.slag = slugify(f'{self.ism}-{self.familiya}-{str(uuid.uuid4())[:4]}')
            super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.ism} {self.familiya}'