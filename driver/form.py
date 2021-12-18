from django.contrib.auth.forms import UserCreationForm
from .models import User, Driver
from django import forms
from django.db import transaction


class DriverCraetionForm(UserCreationForm):
    id = forms.IntegerField(required=True)
    full_name = forms.CharField(required=True)
    address = forms.TextInput()
    birthdate = forms.DateField(required=True)
    email = forms.EmailField(required=True)
    photo = forms.ImageField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.id=self.cleaned_data.get('id')
        user.full_name=self.cleaned_data.get('full_name')
        user.address=self.cleaned_data.get('address')
        user.birthdate=self.cleaned_data.get('birthdate')
        user.email=self.cleaned_data.get('email')
        user.employees='driver'
        user.save()
        driver=Driver.objects.create(user=user)
        driver.photo=self.cleaned_data.get('photo')
        driver.save()
        return user

