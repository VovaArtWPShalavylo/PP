from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Entry
from .forms import EntryForm
# forms test
class EntryTest(TestCase):
    def test_valid_form(self):
        w = Entry.objects.create(name='Party' ,author = User.objects.create(), date = timezone.now() , description = " cool party" , participants = "Alex")
        data = {'name': w.name,'author':w.author,'date': w.date, 'description': w.description,'participants': w.participants }
        form = EntryForm(data=data)
        self.assertFalse(form.is_valid())