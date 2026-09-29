from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length = 50)
    done = models.BooleanField(default=False)
    def _str_(self):
        return self.title