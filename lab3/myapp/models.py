from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import ArrayField



useer  =User.objects.all().values_list('username', flat=True)

choice = tuple((str(useer[i]), str(useer[i])) for i in range(len(useer)))


class Entry(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date = models.DateTimeField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    participants = MultiSelectField(choices =choice, max_choices = 10, max_length = 100,default=User)
    def __str__(self):
        return f'{self.name} {self.date} {self.author} {self.participants}'

    def short_description(self):
        return self.description[:15]


