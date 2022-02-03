from django import forms
from django.conf import settings
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm
)
from mapwidgets.widgets import GooglePointFieldWidget
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.gis.forms import PointField
from .models import (
         Admin
)

from django.contrib.auth import get_user_model

User = get_user_model()


class NewUserForm(UserCreationForm):
    tel_no = PhoneNumberField(widget=PhoneNumberPrefixWidget(
        attrs={'placeholder': 'Tel No: Eg: 2411111'}), label='Country Code', initial='+233')
    location = PointField(widget=GooglePointFieldWidget())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'tel_no', 'photo',  'location', 'password1']



# class ProfileForm(forms.ModelForm):
#     specialty = forms.ModelMultipleChoiceField(queryset=Category.objects.order_by(
#         '-name'), widget=forms.CheckboxSelectMultiple())

#     class Meta:
#         model = Profile
#         exclude = ['user']

