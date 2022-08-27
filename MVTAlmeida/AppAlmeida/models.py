from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre= models.CharField(max_length=50)
    edad= models.models.IntegerField(_)
    

    



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        _detail", kwargs={"pk": self.pk})
)